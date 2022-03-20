from xpath import json_to_tree


def test_json_to_tree_null_value():
    test_str = "null"
    tree = json_to_tree(test_str)
    tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root>None</root>"


def test_json_to_tree_raw_value():
    test_str = "1"
    tree = json_to_tree(test_str)
    tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root>1</root>"
