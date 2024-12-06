from console_io import ConsoleIO
from bibtex_manager import BibtexManager

alias = ["list", "l"]
def execute(io: ConsoleIO, data_manager: BibtexManager, args: list[str]):
    """
    Listaa referenssit.

    args avainsanat: filter, sort

    Voi valita näytettäväksi tietyn tyyppiset entryt kuten book:
    > list filter book article  # joko pilkulla erotetut tai sitten vai peräkkäin olevat

    > list filter author SÄÄNTÖ  # joko ihan merkkijonolla tai säännollisellä lausekkeella. Tän voi toki laittaa eri avainsanan alle.

    # Sort: esimerkissä author aakkosjärjestykseen (sukunimi ensin?) ja year numeerinen (pitää tietää, mitkä fieldit kuuluu sisältää numeerista dataa)
    # identtiset
    > list sort author year desc  
    > list sort author asc year desc

    # ketjutettavat esim:
    > list filter book author "Aku Ankka" sort year asc
    """
    data = data_manager.get_data()
    print(args)
    for entry in data.entries:
        io.write(data.entries[entry].to_string("bibtex"))
