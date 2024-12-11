import argparse
from pybtex.database import OrderedCaseInsensitiveDict, Entry
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
aliases = ["delete", "d"]

def add_to_subparsers(parser, subparsers):
    """ Pyytää subparseria lisäämään komennon """
    delete_parser = subparsers.add_parser(
        "delete",
        aliases=aliases,
        add_help=False,
        help="delete a reference"
    )
    delete_parser.add_argument('delete', help="delete a reference using id")

def execute(io: ConsoleIO, data_manager: BibtexManager, args: argparse.Namespace):
    """ Suorittaa koomennon """
    key = io.read("Anna lähdeviitteen id: ")
    try:
        data_manager.delete_reference(key)
        io.write(f"Poistettu lähde {key}.")
    except KeyError:
        io.write(f'Lähdeavainta "{key}" ei löytynyt!')