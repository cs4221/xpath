from pymongo import MongoClient
import pytest
import os
import json

database_name = "cs4221_test"
data_directory = os.path.join(os.path.dirname(__file__), "mongo_data")


@pytest.fixture()
def mongo_client():
    client = MongoClient("localhost", 27017)
    client.server_info()  # will throw exception if connection is impossible

    # If database does not exist, create it
    if not database_name in client.list_database_names():
        database = client[database_name]

        for filename in os.listdir(data_directory):
            collection_name = os.path.splitext(os.path.split(filename)[1])[0]
            f = os.path.join(data_directory, filename)

            with open(f, "r") as file:
                data = json.loads(file.read().strip())
                collection = database[collection_name]
                if isinstance(data, list):
                    collection.insert_many(data)
                else:
                    collection.insert_one(data)

    yield client
    client.close()


def test_players(mongo_client):
    database = mongo_client[database_name]
    assert "players" in database.list_collection_names()
    manuel = database.players.find_one({"name": "Manuel"})
    assert manuel["surname"] == "Neuer"
