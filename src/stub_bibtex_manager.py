"""
Toteuttaa testausta varten BibtexManager tyngän
"""
from pybtex.database import BibliographyData, Entry


class StubBibtexManager:
    """ Hoitaa bibtex-tiedoston lukemisen ja kirjoittamisen. """
    def __init__(self):
        self.data = BibliographyData()

    def populate(self):
        """ Luo testidataa """
        self.data = create_data()

    def get_data(self):
        """ Palauttaa datan """
        return self.data

    def add_reference(self, key, entry_type, fields):
        """ Lisää lähteen """
        entry = Entry(entry_type, fields)
        self.data.add_entry(key, entry)

    def write(self):
        """ Tynkä """
        pass

    def update_reference(self, key, entry_type, fields):
        """ Päivittää olemassa olevaa lähdettä """
        if key in self.data.entries:
            entry = self.data.entries[key]
            entry.fields.update(fields)
        else:
            self.data.entries[key] = Entry(entry_type, fields)

    def delete_reference(self, key):
        if key in self.data.entries:
            del self.data.entries[key]

def create_data():
    """
    Luo testaustarkoituksiin BibliographyData-objektin.
    Tätä hyödyntävät testit kannattaa rakentaa huomioiden sen,
    että tämä saattaa vielä laajentua tästä esim lisäentryillä.
    """
    return BibliographyData(entries = {
        "VPL11": Entry("inproceedings", {
            "author": "Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti",
            "title": "Extreme Apprenticeship Method in Teaching Programming for Beginners.",
            "year": "2011",
            "booktitle": "SIGCSE '11: Proceedings of the 42nd SIGCSE technical symposium on Computer science education"
        }),
        "CBH91": Entry("article", {
            "author": "Martin, Robert",
            "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
            "year": "2008",
            "publisher": "Prentice Hall"
        }),
        "Martin09": Entry("book", {
            "author": "Martin, Robert",
            "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
            "year": "2008",
            "publisher": "Prentice Hall"
        }),
         "edittausta": Entry("book", {
            "sivu": "20",
        })
    })
