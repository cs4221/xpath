from pymongo import MongoClient
import pytest
import os
import json
from xpath import PyMongoElement

database_name = "cs4221_test"
data_directory = os.path.join(os.path.dirname(__file__), "mongo_data")

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


# Test for loading of json
def test_players(mongo_client):
    database = mongo_client[database_name]
    assert "players" in database.list_collection_names()
    manuel = database.players.find_one({"name": "Manuel"})
    assert manuel["surname"] == "Neuer"


def test_inventory(mongo_client):
    database = mongo_client[database_name]
    assert "inventory" in database.list_collection_names()
    paper = database.inventory.find_one({"item": "paper"})
    assert paper["qty"] == 100


# Tests for PyMongoElement
def test_creating_mongoconverter(mongo_client):
    root = PyMongoElement(mongo_client)
    assert root.tag == "databases"


def test_getting_test_database(mongo_client):
    """Gets the cs4221_test database node."""
    root = PyMongoElement(mongo_client)
    db: PyMongoElement = root.find(
        f"./database[@database_name='{database_name}']"
    )
    assert db.attrib["database_name"] == database_name


def test_getting_players(mongo_client):
    """Gets the `players` collection node."""
    root = PyMongoElement(mongo_client)
    players: PyMongoElement = root.find(
        f"./database[@database_name='{database_name}']/collection[@collection_name='players']"
    )
    # Check that Mario Wehn is a keeper
    assert (
        players.find(".//[name='Mario' and surname='Wehn']").text() == "keeper"
    )
