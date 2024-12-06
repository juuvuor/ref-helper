import sys, pdb # debug

alias = ["add_reference", "add", "a"]
def execute(io, data_manager, args):
    (key, entry_type, fields) = prompt_for_reference(io)
    #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
    data_manager.add_reference(key, entry_type, fields)
    io.write(f"Lisätty lähde {key}, {entry_type}, {fields}")

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
