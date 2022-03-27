# Check that data is read in
def test_players(mongodb):
    assert "players" in mongodb.list_collection_names()
    manuel = mongodb.players.find_one({"name": "Manuel"})
    assert manuel["surname"] == "Neuer"
