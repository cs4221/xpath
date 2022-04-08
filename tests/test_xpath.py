import pytest
import os
import json
from xpath import PyMongoElement, XPath
from pymongo import MongoClient

database_name = "cs4221_test"
data_directory = os.path.join(os.path.dirname(__file__), "mongo_data")
query_dir = os.path.join(os.path.dirname(__file__), "queries")

# Easy creation of a MongoClient
@pytest.fixture()
def mongo_client():
    client = MongoClient("localhost", 27017)
    client.server_info()  # will throw exception if connection is impossible

    # If database does not exist, create it
    if not database_name in client.list_database_names():
        database = client[database_name]
        # For each json file...
        for filename in os.listdir(data_directory):
            # Extract the json name, e.g. players.json -> players.
            collection_name = os.path.splitext(os.path.split(filename)[1])[0]
            f = os.path.join(data_directory, filename)

            with open(f, "r") as file:
                data = json.loads(file.read().strip())
                # Set the collection name to be that of the json file.
                collection = database[collection_name]
                if isinstance(data, list):
                    collection.insert_many(data)
                else:
                    collection.insert_one(data)

    yield client
    client.close()


def test_xpath_input15_find_player_surname(mongo_client):
    f = os.path.join(query_dir, "input15.xq")
    root = PyMongoElement(mongo_client)
    xpath = XPath(root)
    results = xpath.fromQueryFile(f).get()
    assert len(results) == 1
    pass
