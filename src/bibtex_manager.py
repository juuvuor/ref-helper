from pybtex.database import parse_file, BibliographyData
from os.path import isfile
# import atexit

""" # Yksi esimerkki, miten ja milloin tallentaa tiedosto.
def on_exit():
    # Kun ohjelma suljetaan, kirjoitetaan tiedosto.
    data.to_file(bibtex_file_path)
atexit.register(on_exit)
"""


class BibtexManager:
    """ Hoitaa bibtex-tiedoston lukemisen ja kirjoittamisen. """
    def __init__(self, file_path):
        self.file_path = file_path
        # Data muotoa: BibliographyData  https://docs.pybtex.org/api/parsing.html#pybtex.database.BibliographyData
        self.data = parse_file(file_path) if isfile(file_path) else BibliographyData()

    def get_data(self):
        """
        Palauttaa suoraan sisäisesti käytetyn datan, johon ulkoisesti tehdään muutoksia.
        NOTE: voi tän toki muullakin tavalla hoitaa kuten tehä tähän luokkaan jokaisen tempun.
        """
        return self.data
    
    def write(self):
        """
        Kirjoittaa alkuperäisen tiedoston päälle. (tällä hetkellä kuitenkin kirjoittaa testitiedostoon)
        TODO: backup
        """
        self.data.to_file("./test_output.bib") # temp eri tiedosto
