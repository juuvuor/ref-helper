#import sys, pdb # debug
import argparse
from pybtex.database import parse_string as bibtex_from_string, PybtexError, BibliographyData
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
import http_util


aliases = ["add", "a"]

def add_to_subparsers(parser, subparsers):
    """ Pyytää subparseria lisäämään komennon """
    parser_add = subparsers.add_parser(
        "add",
        aliases=aliases,
        add_help=False,
        help="add a reference"
    )
    parser_add.add_argument("--doi", nargs=1, metavar="<doi>", help="Uses dx.doi.org to resolve the URL")
    parser_add.add_argument("--url", nargs=1, metavar="<url>", help="HTTP(S) requests the URL with header {accept: application/x-bibtex}")


def execute(io: ConsoleIO, data_manager: BibtexManager, http: http_util, ns: argparse.Namespace):
    """
    Suorittaa komennon
    Esimerkki doi komento: add --doi 10.1145/2380552.2380613

    # Palvelin ei näköjää palautakkaan bibtex-muotoista vastausta..
    # Kai se vaan riippuu palvelimesta idk
    Esimerkki url komento: add --url https://dl.acm.org/doi/10.1145/2380552.2380613
    """
    if ns.doi or ns.url:
        result = resolve_references_from_arguments(http, ns)
        #print(result.to_string("bibtex"))
        result = prompt_edit_reference_keys(io, data_manager, result)
        data_manager.append_bibliography_data(result)
        return

    (key, entry_type, fields) = prompt_for_reference(io)
    #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
    try:
        if not key:
            io.write("Lähteelle täytyy lisätä lähdeviitteen id!")
            return

        if not entry_type:
            io.write("Lähteelle täytyy lisätä lähdeviitteen tyyppi!")
            return

        data_manager.add_reference(key, entry_type, fields)
        io.write(f"Lisätty lähde {key}, {entry_type}, {fields}.")
    except PybtexError:
        io.write(f'Lähdeavain "{key}" on jo olemassa!')


def prompt_for_reference(io: ConsoleIO):
    """
    Kysyy käyttäjältä lähdeviitten tiedot ja lisää ne.
    """
    key = io.read("Anna lähdeviitten id: ")
    entry_type = io.read("Anna lähdeviitten tyyppi: ")
    fields = {}
    while True:
        field_name = io.read("Anna kentän nimi: ")
        if not field_name:
            break
        field_value = io.read("Anna kentän arvo: ")
        fields[field_name] = field_value
    return (key, entry_type, fields)


def prompt_edit_reference_keys(io: ConsoleIO, data_manager: BibtexManager, data: BibliographyData):
    """
    Käy läpi entryt yksitellen ja tarjoaa käyttäjälle
    kyvyn vaihtaa default avain joksikin toiseksi.
    """
    result = BibliographyData()
    io.write(f"Löydetty {len(data.entries)} lähdeviitettä: (tyhjä vastaus = ei muutosta)")
    for entry_key in data.entries:
        entry = data.entries[entry_key]
        exists = data_manager.key_exists(entry_key)
        new_entry_key = ""
        while True:
            new_entry_key = io.read(f'Muutetaanko lähdeviitettä "{entry_key}"?{" (on jo olemassa)" if exists else ""} > ')
            if not exists:
                if new_entry_key == "":
                    new_entry_key = entry_key
                break
            if new_entry_key == "":
                io.write("Lähdeviitettä pakko muuttaa.")
                continue
            if data_manager.key_exists(new_entry_key):
                io.write(f'Avain "{new_entry_key}" on jo olemassa!')
                continue
            break
        result.add_entry(new_entry_key, entry)
    return result


def resolve_references_from_arguments(http: http_util, ns: argparse.Namespace):
    """ Resolvettaa bibtex-referenssin doi tai url:n perusteella. """
    print("DEBUG: " + str(ns))
    if ns.doi and ns.url:
        raise RuntimeError("Defined both --doi and --url, define only one.")
    if ns.doi:
        url = doi_to_url(ns.doi[0])
    elif ns.url:
        url = ns.url[0]
    else:
        raise RuntimeError("Tried to resolve from arguments without doi or url.")

    result = http.http_get_url(url, "application/x-bibtex")
    if result[0] != "application/x-bibtex":
        raise RuntimeError("Requested application/x-bibtex but server delivered " + str(result[0]))
    return bibtex_from_string(result[1], "bibtex")


def doi_to_url(doi: str):
    """ Muuntaa DOI:n URL-muotoon. """
    return "http://dx.doi.org/" + doi
