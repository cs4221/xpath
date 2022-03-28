import builtins
import io
import os
import pytest

from xpath import elem_to_tree


def patch_open(open_func, files):
    def open_patched(
        path,
        mode="r",
        buffering=-1,
        encoding=None,
        errors=None,
        newline=None,
        closefd=True,
        opener=None,
    ):
        if "w" in mode and not os.path.isfile(path):
            files.append(path)
        return open_func(
            path,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
            closefd=closefd,
            opener=opener,
        )

    return open_patched


@pytest.fixture(autouse=True)
def cleanup_files(monkeypatch):
    files = []
    monkeypatch.setattr(builtins, "open", patch_open(builtins.open, files))
    monkeypatch.setattr(io, "open", patch_open(io.open, files))
    yield
    for file in files:
        os.remove(file)


def test_elem_to_tree_convert_str():
    str_tree = elem_to_tree("hello")
    str_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root>hello</root>"


def test_elem_to_tree_convert_int():
    int_tree = elem_to_tree(1)
    int_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root>1</root>"


def test_elem_to_tree_convert_bool():
    bool_tree = elem_to_tree(False)
    bool_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root>False</root>"


def test_elem_to_tree_convert_None():
    None_tree = elem_to_tree(None)
    None_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root>None</root>"


def test_elem_to_tree_convert_list():
    list = [1, 2]
    list_tree = elem_to_tree(list)
    list_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root><element>1</element><element>2</element></root>"


def test_elem_to_tree_convert_dict():
    dict = {1: 2, "hello": 4}
    dict_tree = elem_to_tree(dict)
    dict_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert data == "<root><1>2</1><hello>4</hello></root>"


def test_setting_attr():
    attr = {"attr1": "val1", "attr2": "val2"}
    list = [1, 2]
    list_tree = elem_to_tree(list, "root", attr)
    list_tree.write("output.xml")
    with open("output.xml", "r") as file:
        data = file.read().rstrip()
        assert (
            data == '<root attr1="val1" attr2="val2">'
            "<element>1</element><element>2</element></root>"
        )
