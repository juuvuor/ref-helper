from console_io import ConsoleIO
from bibtex_manager import BibtexManager

alias = ["list", "l"]
def execute(io: ConsoleIO, data_manager: BibtexManager, args: list[str]):
    """
    Listaa referenssit.

     # TODO: Olisi hyvä, jos tän sais yleistettyä interpreteriin, niin muutkin komennot hyötyis mahdollisesti tämän tapasesta määrittelystä
     # Samalla Help voidaan koostaa sen avulla ja help voidaan kohdistaa tiettyyn komentoon.
     # Ehkä vähän over-engineered..

    # avainsanojen järjestyksellä ei väliä
    [VALINNAINEN]
    <VAADITTU>

    Avainsana filter:
        <entry_type>
        <fieldname> [contains|regex] <value>  # contains defaulttina

    Avainsana sort:
        <fieldname> [numeric] [asc|desc]  # asc defaulttina

    Esimerkkejä:
    Voi valita näytettäväksi tietyn tyyppiset entryt kuten book:
    > list filter book article
    > list filter author "Aku Ankka"
    > list filter author contains "Aku Ankka"
    > list filter author regex .*Ankka

    > list sort author year numeric desc
    > list sort author asc year numeric desc

    # Voidaan ketjuttaa esim:
    > list filter book author "Aku Ankka" sort year asc
    > list sort year asc filter author contains "Aku Ankka" title titteli book inproceedings
    """
    data = data_manager.get_data()
    # print(args)
    for entry in data.entries:
        io.write(data.entries[entry].to_string("bibtex"))
