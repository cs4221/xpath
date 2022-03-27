from pymongo import MongoClient


def test_connection():
    client = MongoClient("localhost", 27017)
    client.server_info()  # force connection on a request as the
    # connect=True parameter of MongoClient seems
    # to be useless here
