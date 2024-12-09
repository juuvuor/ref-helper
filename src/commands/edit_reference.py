import sys, pdb # debug
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
from pybtex.database import OrderedCaseInsensitiveDict, Entry
import argparse

aliases = ["edit", "e"]

def add_to_subparsers(parser, subparsers):
    parser_edit = subparsers.add_parser("edit", aliases=aliases, add_help=False, help="edit a reference")
    parser_edit.add_argument("key_to_edit", help="The key of the reference to edit")

def execute(io: ConsoleIO, data_manager: BibtexManager, args: argparse.Namespace):
    """
    Tarkistaa onko syötettyä keytä olemassa datassa ja editoi sitä jos on.
    """
    try:
        key_to_edit = args.key_to_edit

        if not key_to_edit:
            io.write("Virhe: Syötä lähdeavaimen nimi.")
            return

        if key_to_edit not in data_manager.get_data().entries:
            io.write(f"Lähdeavainta \"{key_to_edit}\" ei löydetty!")
            return

        (entry_type, fields) = prompt_for_reference(io)
        data_manager.update_reference(key_to_edit, entry_type, fields)
        io.write(f"Päivitetty lähde {key_to_edit}, {entry_type}, {fields}.")
    except Exception as e:
        io.write(f"Virhe: {str(e)}")


def prompt_for_reference(io):
    """
    Kysyy käyttäjältä lähdeviitten uudet tiedot.
    """
    entry_type = io.read("Anna lähdeviitten tyyppi: ")
    fields = {}
    while True:
        field_name = io.read("Anna kentän nimi: ")
        if not field_name:
            break
        field_value = io.read("Anna kentän arvo: ")
        fields[field_name] = field_value
    return (entry_type, fields)