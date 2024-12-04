from pybtex.database import BibliographyData, Entry
from pybtex.database.input.bibtex import Parser
from os.path import isfile


class BibtexManager:
    """ Hoitaa bibtex-tiedoston lukemisen ja kirjoittamisen. """
    def __init__(self, file_path):
        self.file_path = file_path
        # Data muotoa: BibliographyData  https://docs.pybtex.org/api/parsing.html#pybtex.database.BibliographyData
        self.data = Parser().parse_file(file_path) if isfile(file_path) else BibliographyData()

    def get_data(self):
        """
        Palauttaa suoraan sisäisesti käytetyn datan, johon ulkoisesti tehdään muutoksia.
        """
        return self.data
    
    def add_reference(self, key, entry_type, fields):
        """ Lisää uuden lähdeviitteen. 
        :param key: lähdeviitten id, voi olla numero tai merkkijono.
        :param entry_type: lähdeviitteen tyyppi esim kirja, artikkeli
        :param fields: lähdeviitteen sisältö
        """
        entry = Entry(entry_type, fields)
        self.data.entries[key] = entry
        self.write()

    def write(self):  
        """
        Kirjoittaa bib tiedostoon.
        TODO: backup
        """
        with open(self.file_path, "w") as bibfile:
            self.data.to_file(bibfile)
