from pybtex.database import parse_file, BibliographyData, Entry
from pybtex.database.input.bibtex import Parser
from os.path import isfile
import atexit

class BibtexManager:
    """ Hoitaa bibtex-tiedoston lukemisen ja kirjoittamisen. """
    def __init__(self, file_path):
        self.file_path = file_path
        # Data muotoa: BibliographyData  https://docs.pybtex.org/api/parsing.html#pybtex.database.BibliographyData
        self.data = Parser().parse_file(file_path) if isfile(file_path) else BibliographyData()

    def get_data(self):
        """
        Palauttaa suoraan sisäisesti käytetyn datan, johon ulkoisesti tehdään muutoksia.
        NOTE: voi tän toki muullakin tavalla hoitaa kuten tehä tähän luokkaan jokaisen tempun.
        """
        return self.data
    
    def add_reference(self, key, entry_type, fields):
        """ Lisää uuden referenssin. 
        :param key: referenssin id, voi olla numero tai merkkijono.
        :param entry_type: referenssin tyyppi esim kirja, artikkeli
        :param fields: referenssin sisältö
        """
        entry = Entry(entry_type, fields)
        self.data.entries[key] = entry
        print(f"Lisätty referenssi {key}, {entry_type}, {fields}")
        
    
    def write(self):  
        """
        Kirjoittaa alkuperäisen tiedoston päälle. (tällä hetkellä kuitenkin kirjoittaa testitiedostoon)
        TODO: backup
        """
        with open(self.file_path, "w") as bibfile:
            self.data.to_file(bibfile)   
            
    def prompt_for_reference(self):
        key = input("Anna referenssin id: ")
        entry_type = input("Anna referenssin tyyppi: ")
        fields = {}
        while True:
            field_name = input("Anna kentän nimi: ")
            if not field_name:
                break
            field_value = input("Anna kentän arvo: ")
            fields[field_name] = field_value
        self.add_reference(key, entry_type, fields)
        self.write()