from pymongo import MongoClient


def test_connection():
    client = MongoClient("localhost", 27017)
    print(client.server_info())  # force connection
