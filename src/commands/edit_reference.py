import sys, pdb # debug

alias = ["edit_reference", "edit_ref", "edit", "e"]
def execute(io, data_manager, args):
    """
    Tarkistaa onko syötettyä keytä olemassa datassa ja editoi sitä jos on.
    """
    #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
    try:
        key_to_edit = args[1]
        # tässä poikkeus jos avainta ei löydy
        (entry_type, fields) = prompt_for_reference(io)
        data_manager.update_reference(key_to_edit, entry_type, fields)
        io.write(f"Päivitetty lähde {key_to_edit}, {entry_type}, {fields}.")
    except Exception as e:
        io.write(f'Lähdeavaita "{key_to_edit}" ei löydetty!')    

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
