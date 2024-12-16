#import sys, pdb
import argparse
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
from pybtex.database import OrderedCaseInsensitiveDict, Entry


aliases = ["edit", "e"]

def add_to_subparsers(parser, subparsers):
    """ Pyytää subparseria lisäämään komennon """
    parser_edit = subparsers.add_parser("edit",
        aliases=aliases,
        add_help=False,
        help="edit a reference"
    )
    parser_edit.add_argument("key_to_edit", help="The key of the reference to edit")

def execute(io: ConsoleIO, data_manager: BibtexManager, http, args: argparse.Namespace):
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

        entry_to_edit = data_manager.get_data().entries[key_to_edit]
        (entry_type, fields) = prompt_for_reference(io, entry_to_edit)
        data_manager.update_reference(key_to_edit, entry_type, fields)
        io.write(f"Päivitetty lähde {key_to_edit}, {entry_type}, {fields}.")
    except Exception as e:
        io.write(f"Virhe: {str(e)}")


def prompt_for_reference(io, entry_to_edit):
    """
    Kysyy käyttäjältä lähdeviitten uudet tiedot.
    """
    entry_type = io.read(f"Anna lähdeviitteen uusi tyyppi [{entry_to_edit.type}]: ")
    if not entry_type:
        entry_type = entry_to_edit.type
    fields = {}
    # Haetaan olemassa olevat fieldit ja loopataan ne läpi
    old_field_keys = entry_to_edit.fields.keys()
    for field_key in old_field_keys:
        field_value = io.read(
            f"Syötä kentän '{field_key}' päivitetty arvo, [{entry_to_edit.fields[field_key]}] / DEL: "
        )
        if not field_value:
            fields[field_key] = entry_to_edit.fields[field_key]
        elif field_value == "DEL":
            # Älä lisää fieldseihin
            pass
        else:
            fields[field_key] = field_value

    while True:
        field_name = io.read("Anna uuden kentän nimi (tai tyhjä): ")
        if not field_name:
            break
        field_value = io.read("Anna kentän arvo: ")
        fields[field_name] = field_value
    return (entry_type, fields)
