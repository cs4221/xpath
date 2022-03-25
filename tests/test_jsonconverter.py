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

        
def test_json_to_tree_array_string():
    test_str = ('{"employees":['
                '{ "firstName":"John", "lastName":"Doe" },'
                '{ "firstName":"Anna", "lastName":"Smith" },'
                '{ "firstName":"Peter", "lastName":"Jones" }'
                ']}')
    expected_str = ("<root><employees>"
                    "<element><firstName>John</firstName>"
                    "<lastName>Doe</lastName></element><element>"
                    "<firstName>Anna</firstName><lastName>Smith</lastName>"
                    "</element><element><firstName>Peter</firstName><lastName>"
                    "Jones</lastName></element>"
                    "</employees></root>")
    tree = json_to_tree(test_str)
    tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().strip()
        assert data == expected_str
