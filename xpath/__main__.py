import argparse
import json  # pragma: no cover

from . import BaseClass, base_function  # pragma: no cover
from .jsonconverter import json_to_tree

def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m xpath` and `$ xpath `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="xpath.",
        epilog="Enjoy the xpath functionality!",
    )
    # This is required positional argument
    parser.add_argument(
        "name",
        type=str,
        help="The username",
        default="cs4221",
    )
    # This is optional named argument
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="The Message",
        default="Hello",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()
    print(f"{args.message} {args.name}!")
    if args.verbose:
        print("Verbose mode is on.")

    json_obj = """
    {
        "glossary": {
            "title": "example glossary",
        "GlossDiv": {
                "title": "S",
        "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
            "SortAs": "SGML",
            "GlossTerm": "Standard Generalized Markup Language",
            "Acronym": "SGML",
            "Abbrev": "ISO 8879:1986",
            "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                "GlossSeeAlso": ["GML", "XML"]
                        },
            "GlossSee": "markup"
                    }
                }
            }
        }
    }
    """
    tree = json_to_tree(json_obj)

    print("Executing main function")
    base = BaseClass()
    print(base.base_method())
    print(base_function())
    print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
