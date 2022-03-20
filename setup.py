"""Python setup.py for xpath package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("xpath", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="xpath",
    version=read("xpath", "VERSION"),
    description="XPath traversal for JSON and MongoDB created by Lee En Hao and Leong Jia Hao, Timothy",
    url="https://github.com/cs4221/xpath/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="cs4221",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["xpath = xpath.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
