"""
Methods to take a PyMongo client and run xpath queries on it.
"""
import warnings
import xml.etree.ElementTree as ET

from bson.objectid import ObjectId
from pymongo import MongoClient

from .elemconverter import elem_to_tree


class PyMongoElement(ET.Element):
    """
    This class wraps around a PyMongo client.
    It subclasses xml's Element class, implementing lazy traversal.

    A toplevel client will have no attributes
        -> e.g. <databases>
    A node at the level of a database will have an attribute called:
        - database_name
        -> e.g. <database database_name = "app">
    A node at the level of a collection will have the attributes:
        - database_name
        - collection_name
        -> e.g. <collection database_name = "app" collection_name = "users">
    A node at the level of a document will have the tags:
        - database_name
        - collection_name
        - object_id
        -> e.g. <document ...>
    """

    # Constants for the attributes
    database_name = "database_name"
    collection_name = "collection_name"
    object_id = "object_id"

    # Constants for the tags
    databases = "databases"
    database = "database"
    collection = "collection"
    document = "document"

    def __init__(
        self,
        client: MongoClient,
        tag: str = "",
        attrib={},
    ):
        if not isinstance(client, MongoClient):
            raise TypeError(
                "client must be PyMongo's Mongoclient, not %s"
                % (client.__class__.__name__,)
            )

        if tag == "":
            tag = self.__class__.databases

        super(PyMongoElement, self).__init__(tag, attrib)
        self.client = client
        self.tag = tag
        self.attrib = attrib

    def __repr__(self):
        return "<%s %r attributes = %s at %#x>" % (
            self.__class__.__name__,
            repr(self.tag),
            " ".join(
                [str(k) + "=" + str(v) for (k, v) in self.attrib.items()]
            ),
            id(self),
        )

    def __copy__(self):
        """Shallow copy of current element."""
        result = self.__class__(self.client, self.tag, self.attrib)
        result.text = self.text
        result.tail = self.tail
        result[:] = self
        return result

    def __len__(self):
        if self.tag == PyMongoElement.databases:
            # Return the number of databases
            return len(self.client.list_database_names())

        assert (
            PyMongoElement.database_name in self.attrib
        ), "database_name is not set"
        database = self.client[self.attrib[PyMongoElement.database_name]]

        if self.tag == PyMongoElement.database:
            # Return the number of collections
            return len(database.list_collection_names())
        assert (
            PyMongoElement.collection_name in self.attrib
        ), "collection_name is not set"
        collection = database[self.attrib[PyMongoElement.collection_name]]

        if self.tag == PyMongoElement.collection:
            # Return the number of documents in this collection
            # First check that you have database_name and
            # collection_name in your attributes
            return collection.count_documents({})

        assert PyMongoElement.object_id in self.attrib, "object_id is not set"
        document = collection.find_one(
            {"_id": ObjectId(self.attrib[PyMongoElement.object_id])}
        )
        return len(document)

    def __bool__(self):
        warnings.warn(
            "Not used in this implementation, the value is undefined."
        )
        return False

    def __getitem__(self, index):
        if self.tag == PyMongoElement.databases:
            names = self.client.list_database_names()
            attrib_clone = self.attrib.copy()
            attrib_clone[PyMongoElement.database_name] = names[index]
            result = PyMongoElement(
                self.client, PyMongoElement.database, attrib_clone
            )
            return result

        assert (
            PyMongoElement.database_name in self.attrib
        ), "database_name is not set"
        database = self.client[self.attrib[PyMongoElement.database_name]]

        if self.tag == PyMongoElement.database:
            names = database.list_collection_names()
            attrib_clone = self.attrib.copy()
            attrib_clone[PyMongoElement.collection_name] = names[index]
            result = PyMongoElement(
                self.client, PyMongoElement.collection, attrib_clone
            )
            return result

        assert (
            PyMongoElement.collection_name in self.attrib
        ), "collection_name is not set"
        collection = database[self.attrib[PyMongoElement.collection_name]]

        if self.tag == PyMongoElement.collection:
            for i, doc in collection.find():
                if i == index:
                    attrib_clone = self.attrib.copy()
                    attrib_clone[PyMongoElement.object_id] = str(doc._id)
                    result = PyMongoElement(
                        self.client, PyMongoElement.document, attrib_clone
                    )
                    return result

        assert PyMongoElement.object_id in self.attrib, "object_id is not set"
        # This object is a document - fall back on the map converter
        if self.tag == PyMongoElement.document:
            document = collection.find_one(
                {"_id": ObjectId(self.attrib[PyMongoElement.object_id])}
            )

            return elem_to_tree(document).getroot().__getitem__(index)

    def __setitem__(self, index, element):
        warnings.warn(
            """ not implemented, function does not change database """
        )

    def __delitem__(self, index):
        warnings.warn(
            """ not implemented, function does not change database """
        )

    def append(self, subelement):
        warnings.warn(
            """ not implemented, function does not change database """
        )

    def extend(self, elements):
        warnings.warn(
            """ not implemented, function does not change database """
        )

    def insert(self, index, subelement):
        warnings.warn(
            """ not implemented, function does not change database """
        )

    def remove(self, subelement):
        warnings.warn(
            """ not implemented, function does not change database """
        )

    def iter(self, tag=None):
        """
        Copied from xml.etree.Element:
        Create tree iterator.

        The iterator loops over the element and all subelements in document
        order, returning all elements with a matching tag.

        If the tree structure is modified during iteration, new or removed
        elements may or may not be included.  To get a stable set, use the
        list() function on the iterator, and loop over the resulting list.

        *tag* is what tags to look for (default is to return all elements)

        Return an iterator containing all the matching elements.

        """
        if tag == "*":
            tag = None

        if tag is None or self.tag == tag:
            yield self

        if self.tag == PyMongoElement.databases:
            for database in self.client.list_databases():
                name = database["name"]
                attrib_clone = self.attrib.copy()
                attrib_clone[PyMongoElement.database_name] = name
                child = PyMongoElement(
                    self.client, PyMongoElement.database, attrib_clone
                )
                yield from child.iter(tag)
        elif self.tag == PyMongoElement.database:
            assert (
                PyMongoElement.database_name in self.attrib
            ), "database_name is not set"
            database = self.client[self.attrib[PyMongoElement.database_name]]
            for collection in database.list_collections():
                name = collection["name"]
                attrib_clone = self.attrib.copy()
                attrib_clone[PyMongoElement.collection_name] = name
                child = PyMongoElement(
                    self.client, PyMongoElement.collection, attrib_clone
                )
                yield from child.iter(tag)
        elif self.tag == PyMongoElement.collection:
            assert (
                PyMongoElement.database_name in self.attrib
            ), "database_name is not set"
            database = self.client[self.attrib[PyMongoElement.database_name]]

            assert (
                PyMongoElement.collection_name in self.attrib
            ), "collection_name is not set"
            collection = database[self.attrib[PyMongoElement.collection_name]]

            for doc in collection.find():
                attrib_clone = self.attrib.copy()
                attrib_clone[PyMongoElement.object_id] = str(doc._id)
                child = PyMongoElement(
                    self.client, PyMongoElement.document, attrib_clone
                )
                yield from child.iter(tag)
        elif self.tag == PyMongoElement.document:
            assert (
                PyMongoElement.database_name in self.attrib
            ), "database_name is not set"
            database = self.client[self.attrib[PyMongoElement.database_name]]

            assert (
                PyMongoElement.collection_name in self.attrib
            ), "collection_name is not set"
            collection = database[self.attrib[PyMongoElement.collection_name]]

            document = collection.find_one(
                {"_id": ObjectId(self.attrib[PyMongoElement.object_id])}
            )

            yield from elem_to_tree(
                document, PyMongoElement.document
            ).getroot().iter(tag)
