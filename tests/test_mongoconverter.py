from pymongo import MongoClient


# def test_connection():
#     client = MongoClient(
#         "mongodb://localhost:27017/", serverSelectionTimeoutMS=0
#     )
#     client.server_info()  # force connection on a request as the
#     # connect=True parameter of MongoClient seems
#     # to be useless here
