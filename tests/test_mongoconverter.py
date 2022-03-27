from pymongo import MongoClient


def test_connection():
    client = MongoClient("localhost", 27017)
    print(client.server_info())  # force connection


def test_players(mongodb):
    assert "players" in mongodb.list_collection_names()
    manuel = mongodb.players.find_one({"name": "Manuel"})
    assert manuel["surname"] == "Neuer"
