from console_io import ConsoleIO
from bibtex_manager import BibtexManager
from pybtex.database import OrderedCaseInsensitiveDict
import sys, pdb

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

    # Mietintää:
    # > list AVAIN  # voisi listata vain kyseisen entryn
    # voi myös lisätä vaikka avainsanan key-only, jolloin tulostetaan vain key
    """
    data = data_manager.get_data()
    # print(args)
    for entry in data.entries:
        io.write(data.entries[entry].to_string("bibtex"))
    
    arr = dict_to_list(data.entries)
    result = sort_by_rules(arr, [{"field": "year"}, {"field": "author", "reverse": True}])
    print(result)


def sort_by_rules(arr: list, rules: list[dict]):
    """
    Järjestää annetun listan annettujen sääntöjen mukaan.
    :arr list: Järjestettävä lista
    :param rules: Muotoa [{"field": "FIELDNAME", "numeric": True, "reverse": False}]
    Huom: Entry-objektissa author ei mene fields-attribuuttiin vaa persons, mikä on luokkaa OrderedCaseInsensitiveDict.
    """
    print(rules) # debug
    def key_func(entry):
        """
        Python sorttaa arrayt alkioiden mukaan järjestyksessä.
        Eli vertailee automaattisesti ensimmäisiä ja toisia jne..
        Tai ainakin se tekee näin tuplejen kanssa..
        """
        result = [] # esimerkki ['1991', 'Luukkainen, Matti;Paksula, Matti;Vihavainen, Arto']
        for i in range(len(rules)):
            #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
            rule = rules[i]
            field = rule.get("field")
            if field == "author": # voi olla muitakin poikkeuksia
                value = entry.persons["author"] # Esim: [Person('Collins, Allan'), Person('Brown, John Seely'), Person('Holum, Ann')]
                value = list(map(lambda person : str(person), value)) # Muutetaan Person => str sukunimi ensin
                #value.sort(key = lambda person : str(person)) # Nimet aakkosjärjestykseen
                value = ";".join(value) # Saadaan yhteen merkkijonoon.
            else:
                value = entry.fields[field]
            value = value.lower()

            if rule.get("numeric"):
                try:
                    value = float(value)
                except Exception as e:
                    pass

            if rule.get("reverse"):
                if rule.get("numeric"):
                    value *= -1
                else:
                    # Ilmeisesti käänteinen string sorttautuu kans käänteisesti?
                    # src: https://www.geeksforgeeks.org/python-sort-on-basis-of-reverse-strings/?ref=ml_lbp
                    value = value[::-1]
            result.append(value)

        # debug printit
        print("key_func: " + entry.key)
        print(result)
        return result

    arr.sort(key = key_func)
    return arr


def dict_to_list(dict: OrderedCaseInsensitiveDict):
    """ Muuttaa dict listaksi. """
    result = []
    for key in dict:
        result.append(dict[key])
    return result

