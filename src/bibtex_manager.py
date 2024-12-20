"""
Toteuttaa luokan BibtexManager
"""
from os.path import isfile
from pybtex.database import BibliographyData, Entry
from pybtex.database.input.bibtex import Parser


class BibtexManager:
    """
    Hoitaa bibtex-tiedoston lukemisen ja kirjoittamisen.
    NOTE: BibliographyData ylläpitää myös jotain crossref hommaa
    ja wanted_entries dictiä, voivat aiheuttaa bugeja erikoisemmilla referensseillä.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        # Data muotoa: BibliographyData
        # https://docs.pybtex.org/api/parsing.html#pybtex.database.BibliographyData
        self.data = Parser(encoding="utf-8").parse_file(file_path) if isfile(file_path) else BibliographyData()

    def get_data(self):
        """
        Palauttaa suoraan sisäisesti käytetyn datan, johon ulkoisesti tehdään muutoksia.
        """
        return self.data

    def key_exists(self, key: str):
        """ Tarkistaa onko avain varattu. """
        return key in self.data.entries

    def add_reference(self, key, entry_type, fields):
        """ Lisää uuden lähdeviitteen. 
        :param key: lähdeviitten id, voi olla numero tai merkkijono.
        :param entry_type: lähdeviitteen tyyppi esim kirja, artikkeli
        :param fields: lähdeviitteen sisältö
        """
        entry = Entry(entry_type, fields)
        self.data.add_entry(key, entry)
        self.write()

    def append_bibliography_data(self, data: BibliographyData):
        """ Lisää BibliographyData-objektin tiedot referensseihin. """
        print("DEBUG: add_bibliography_data " + str(data))
        for entry_key in data.entries:
            entry = data.entries[entry_key]
            self.data.add_entry(entry_key, entry)
        self.write()

    def update_reference(self, key, entry_type, fields):
        """ Päivittää lähdeviitteen uusilla tiedoilla. 
        :param key: lähdeviitten id, voi olla numero tai merkkijono.
        :param entry_type: lähdeviitteen tyyppi esim kirja, artikkeli
        :param fields: lähdeviitteen sisältö
        """
        entry = Entry(entry_type, fields)
        self.data.entries.pop(key)
        self.data.add_entry(key, entry)
        self.write()

    def delete_reference(self, key):
        """ Poistaa avainta vastaan lähdeviitteen.
        :param key: lähdeviitten id, voi olla numero tai merkkijono.
        """
        if key not in self.data.entries:
            raise KeyError(f'Lähdeavainta "{key}" ei löytynyt!')
        self.data.entries.pop(key)
        self.write()

    def write(self):
        """
        Kirjoittaa bib tiedostoon.
        TODO: backup
        """
        with open(self.file_path, "w", encoding="utf-8") as bibfile:
            self.data.to_file(bibfile)
