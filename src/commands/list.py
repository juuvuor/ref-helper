from console_io import ConsoleIO
from bibtex_manager import BibtexManager
from pybtex.database import OrderedCaseInsensitiveDict, Entry
import argparse
#import sys, pdb


aliases = ["list", "l"]

def add_to_subparsers(parser, subparsers):
    parser_list = subparsers.add_parser("list", aliases=aliases, add_help=False, help="list references")
    parser_list.add_argument("-t", "--type", nargs="*", default=[], action="append",
                            metavar="<entry_type>",
                            help="""<entry_type> like "book" or "article\"""")
    parser_list.add_argument("-f", "--field", nargs="*", default=[], action="append",
                            metavar="<field_name> <value>",
                            help="""<field_name> accompanied by its <value> like 'author "Aku Ankka"'""")
    parser_list.add_argument("-s", "--sort", nargs="*", default=[], action="append",
                            metavar="<field_name> [numeric] [desc]",
                            help="""<field_name> with two optional modifiers [numeric] [desc] (to make the order descending) like 'year numeric desc' to sort by year treated as a number in descending order or "title" to sort by title in ascending order""")

def execute(io: ConsoleIO, data_manager: BibtexManager, ns: argparse.Namespace):
    """
    Listaa referenssit.

    # Esimerkki inputit interpreteriin, mitkä muuttuvat argparse.Namespace muotoon add_to_subparsers määrittelemällä tavalla.
    ["list", "-t", "book", "article"]
    ["list", "--type", "book", "article"]
    ["list", "--field", "title", "Akun kirja", "author", "Aku Ankka"]
    ["list", "--sort", "year"]
    ["list", "--sort", "year", "desc"]
    ["list", "-t" "book", "-f", "author", "Aku Ankka", "-s", "year", "reverse"]
    ["list", "-t" "book", "-f", "author", "Aku Ankka", "-s", "year", "numeric", "reverse"]

    :param ns: Mallia: Namespace(command_name='list', type=[], field=[['author', 'Aku'], ['author', 'Roope']], sort=[])
    """

    print("DEBUG: list namespace: " + str(ns)) # debug

    data = data_manager.get_data()
    arr = dict_to_list(data.entries)


    # Hidas mutta toimii
    # Suodatus tyypin perusteella 
    if ns.type:
        filtered_entries = []
        for entry in arr:
            for sublist in ns.type:
                if entry.type in sublist:
                    # Jos on, lisää entry filtered_entries-listaan
                    filtered_entries.append(entry)
        
        arr = filtered_entries

    # TODO 
    # Suodatus kenttien perusteella
    # if ns.field:
    #     print field
    #     for field, value in ns.field:
    #         arr = [entry for entry in arr if field in entry.type in ns.type]

    # TODO 
    # # Lajittelu sääntöjen perusteella
    # if ns.sort:
    #     sort_rules = []
    #     for i in range(0, len(ns.sort), 3):
    #         field = ns.sort[i]
    #         numeric = (i + 1 < len(ns.sort) and ns.sort[i + 1] == 'numeric')
    #         reverse = (i + 2 < len(ns.sort) and ns.sort[i + 2] == 'desc')
    #         sort_rules.append({"field": field, "numeric": numeric, "reverse": reverse})

    #     arr = sort_by_rules(arr, sort_rules)

    # Tulostetaan tulokset
    for entry in arr:
         io.write(entry.to_string("bibtex"))



    

def sort_by_rules(arr, rules):
    """
    Lajittelee listan sääntöjen perusteella.
    """
    for rule in reversed(rules):
        field = rule["field"]
        numeric = rule.get("numeric", False)
        reverse = rule.get("reverse", False)
        arr.sort(key=lambda x: int(x[field]) if numeric else x[field], reverse=reverse)
    return arr

def dict_to_list(entries):
    """
    Muuntaa sanakirjan listaksi.
    """
    return [entry for entry in entries.values()]

def sort_by_rules(arr: list, rules: list[dict]):
    """
    Järjestää annetun listan annettujen sääntöjen mukaan.
    Jos field puuttuu entrystä, niin se vain korvataan tyhjällä merkkijonolla "".
    Jos rule on merkattu numeric, niin se koittaa muuttaa floatiksi ja jos ei onnistu, niin arvoksi asetetaan nolla.
    # NOTE: Arvoksi vois tällöin asettaa vaikka pienimmän tai suurimman mahdollisen luvun nii ne saadaan listauksen alkuun tai perälle.
    :param arr: Järjestettävä lista
    :param rules: Muotoa [{"field": str, "numeric": bool, "reverse": bool}]
    Huom: Entry-objektissa author ei mene fields-attribuuttiin vaan persons-attribuuttiin, mikä on luokkaa OrderedCaseInsensitiveDict.
    """
    #print(rules) # debug
    def key_func(entry: Entry):
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
            # avain pienistä aakkosista ja trimmataan whitespacet alusta ja lopusta
            # Voi olla vöhän jännä jos henkilöiden nimissä on paljon whitespacea, koska niitä ei trimmata tällöin.
            value = resolve_entry_field_value(entry, field).lower().strip()

            if rule.get("numeric"):
                try:
                    value = float(value)
                except Exception:
                    value = 0

            if rule.get("reverse"):
                if rule.get("numeric"):
                    value *= -1
                else:
                    # Ilmeisesti käänteinen string sorttautuu kans käänteisesti?
                    # src: https://www.geeksforgeeks.org/python-sort-on-basis-of-reverse-strings/?ref=ml_lbp
                    value = value[::-1]
            result.append(value)

        # debug printit
        #print("key_func: " + entry.key)
        #print(result)
        return result

    arr.sort(key = key_func)
    return arr


def resolve_entry_field_value(entry: Entry, field: str, persons_to_str = True):
    """
    Hakee entrystä halutun fieldin arvon. Fieldin puuttuessa palautetaan tyhjä merkkijono "".
    :param persons_to_str: persons on defaultisti lista Person-olioista.
    """
    if field == "author": # voi olla muitakin poikkeuksia
        value = entry.persons.get("author") # Esim: [Person('Collins, Allan'), Person('Brown, John Seely'), Person('Holum, Ann')]
        if value != None and persons_to_str:
            value = list(map(lambda person : str(person), value)) # Muutetaan Person => str sukunimi ensin
            #value.sort(key = lambda person : str(person)) # Nimet aakkosjärjestykseen
            value = ";".join(value) # Saadaan yhteen merkkijonoon.
    else:
        value = entry.fields.get(field)
    return "" if value == None else value


def dict_to_list(dict: OrderedCaseInsensitiveDict):
    """ Muuttaa dict listaksi. """
    result = []
    for key in dict:
        result.append(dict[key])
    return result

