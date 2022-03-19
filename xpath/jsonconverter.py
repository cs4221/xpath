"""
Method to convert JSON object to xml's original object tree
"""
import json
import xml.etree.ElementTree as ET

from .elemconverter import elem_to_tree


def json_to_tree(jsonstr: str) -> ET.ElementTree:
    return elem_to_tree(json.loads(jsonstr))
