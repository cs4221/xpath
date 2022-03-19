"""
Methods to take a Python dictionary/list/value, and turn it into xml's original object tree.
"""

import xml.etree.ElementTree as ET


def insert(parent: ET.Element, tag: str, elem: any) -> None:
    """
    Recursively takes a tag, an element which is either a list, dict or a value type,
    and creates subtrees.

    Items in lists are tagged with 'element'.
    """
    child_node = ET.SubElement(parent, tag)

    if isinstance(elem, dict):
        for key, value in elem.items():
            insert(child_node, key, value)
    elif isinstance(elem, list):
        for arr_elem in elem:
            insert(child_node, "element", arr_elem)
    else:
        child_node.text = str(elem)

    return child_node


def elem_to_tree(elem: any, roottag: str = "root") -> ET.ElementTree:
    """
    Takes a Python dictionary/list/value, and converts it to an object tree.
    The top level node has tag name 'root'.
    """
    if elem is None:
        return None

    tree: ET.Element = ET.Element("remove_later")
    return ET.ElementTree(insert(tree, roottag, elem))
