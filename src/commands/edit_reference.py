import sys, pdb # debug

alias = ["edit_reference", "edit_ref", "edit", "e"]
def execute(io, data_manager, args):
    """
    Tarkistaa onko syötettyä keytä olemassa datassa ja editoi sitä jos on.
    """
    try:
        if len(args) < 1:
            io.write("Virhe: Syötä lähdeavaimen nimi.")
            return

        key_to_edit = args[1]  # Varmista, että key_to_edit on aina määritelty
        # Tässä poikkeus jos avainta ei löydy
        (entry_type, fields) = prompt_for_reference(io)
        data_manager.update_reference(key_to_edit, entry_type, fields)
        io.write(f"Päivitetty lähde {key_to_edit}, {entry_type}, {fields}.")
    except KeyError:
        io.write(f'Lähdeavainta "{key_to_edit}" ei löydetty!')
    except IndexError:
        io.write("Virhe: Lähdeavaimen nimi puuttuu syötteestä.")
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
