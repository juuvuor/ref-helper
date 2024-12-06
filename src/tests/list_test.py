import unittest
from commands.list import execute
from stub_io import StubIO
from unittest.mock import Mock
from pybtex.database import BibliographyData, Entry


class TestListCommand(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.data_manager = Mock()
        self.data = BibliographyData(entries = {
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
        self.data_manager.get_data.return_value = self.data

    def test_ilman_argumentteja(self):
        execute(self.io, self.data_manager, ["list"])
        total = "".join(self.io.outputs)
        for key in self.data.entries:
            self.assertIn(key, total)

