import argparse
from pybtex.database import OrderedCaseInsensitiveDict, Entry
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
aliases = ["delete", "d"]

def add_to_subparsers(parser, subparsers):
    """ Pyytää subparseria lisäämään komennon """
    delete_parser = subparsers.add_parser("delete",
        aliases=aliases,
        add_help=False,
        help="delete a reference"
    )
    delete_parser.add_argument('delete_key', help="The key of the reference to delete")

def execute(io: ConsoleIO, data_manager: BibtexManager, args: argparse.Namespace):
    """ Suorittaa koomennon """
    delete_key = args.delete_key
    confirmation = io.read(f"Poistetaanko lähde {delete_key}? (k/e)")
    if confirmation.lower() == 'k':
        try:
            data_manager.delete_reference(delete_key)
            io.write(f"Poistettu lähde {delete_key}.")
        except KeyError:
            io.write(f'Lähdeavainta "{delete_key}" ei löytynyt!')
    else:
        io.write("Poistoa ei suoritettu.")