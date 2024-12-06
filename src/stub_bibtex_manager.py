from pybtex.database import BibliographyData, Entry


class StubBibtexManager:
    """ Hoitaa bibtex-tiedoston lukemisen ja kirjoittamisen. """
    def __init__(self):
        self.data = BibliographyData()

    def populate(self):
        self.data = create_data()

    def get_data(self):
        return self.data

    def add_reference(self, key, entry_type, fields):
        entry = Entry(entry_type, fields)
        self.data.add_entry(key, entry)

    def write(self):
        pass


def create_data():
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
        })
    })