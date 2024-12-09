import sys, pdb # debug

aliases = ["add_reference", "add", "a"]

def add_to_subparsers(parser, subparsers):
    parser_add = subparsers.add_parser("add", aliases=aliases, add_help=False, help="add a reference")

def execute(io, data_manager, ns):
    (key, entry_type, fields) = prompt_for_reference(io)
    #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
    try:
        data_manager.add_reference(key, entry_type, fields)
        io.write(f"Lisätty lähde {key}, {entry_type}, {fields}.")
    except Exception as e:
        io.write(f'Lähdeavain "{key}" on jo olemassa!')

def prompt_for_reference(io):
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
