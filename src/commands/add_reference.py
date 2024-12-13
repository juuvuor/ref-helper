#import sys, pdb # debug
import argparse
import requests
from console_io import ConsoleIO
from bibtex_manager import BibtexManager


aliases = ["add", "a"]

def add_to_subparsers(parser, subparsers):
    """ Pyytää subparseria lisäämään komennon """
    parser_add = subparsers.add_parser(
        "add",
        aliases=aliases,
        add_help=False,
        help="add a reference"
    )
    # TODO: Lisää argumentti --doi
    parser_add.add_argument("--doi", nargs=1, help="Uses dx.doi.org to resolve the URL")
    parser_add.add_argument("--url", nargs=1, help="HTTP(S) requests the URL with header {accept: application/x-bibtex}")


def execute(io: ConsoleIO, data_manager: BibtexManager, ns: argparse.Namespace):
    """ Suorittaa komennon """
    if ns.doi or ns.url:
        return resolve_reference_from_arguments(io, ns)

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
    except Exception as e:
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


def resolve_reference_from_arguments(io: ConsoleIO, ns: argparse.Namespace):
    print("DEBUG: " + str(ns))
    if ns.doi and ns.url:
        return io.write("Defined both --doi and --url, define only one.")
    if ns.doi:
        pass
    elif ns.url:
        pass
    else:
        raise Exception("Tried to resolve from arguments without doi or url.")


def get_doi(doi: str, mime_type = "application/x-bibtex"):
    """
    Hakee DOI:ta vastaavan dokumentin halutussa formaatissa.
    :param mime_type: defaultisti bibtexin mime type, jolloin sitä tukevat palvelimet palauttaa bibtex-muotoisen vastauksen.
    :returns: Muotoa: (MIME_TYPE, CONTENT) Palvelimesta riippuen palautettava merkkijono voi olla halutussa muodossa tai ei.
    Esim "10.1000/182" tulee text/html muodossa ja 10.1145/2380552.2380613 tulee application/x-bibtex muodossa jos niin halutaan.
    """
    url =  "http://dx.doi.org/" + doi
    headers = {"accept": mime_type}
    r = requests.get(url, headers=headers, timeout=5000)
    return (r.headers.get("content-type"), r.text)

