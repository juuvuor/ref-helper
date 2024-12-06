import unittest
from commands.list import execute
from stub_io import StubIO
from stub_bibtex_manager import StubBibtexManager


class TestListCommand(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.data_manager = StubBibtexManager()
        self.data_manager.populate()

    def test_ilman_argumentteja(self):
        execute(self.io, self.data_manager, ["list"])
        total = "".join(self.io.outputs)
        for key in self.data_manager.get_data().entries:
            self.assertIn(key, total)

    def test_filter_book(self):
        """ NOTE: EI TOIMI TÄLLÄ HETKELLÄ OIKEIN! """
        entry_type = "book"
        execute(self.io, self.data_manager, ["list", "filter", entry_type])
        total = "".join(self.io.outputs)
        entries = self.data_manager.get_data().entries
        for key in entries:
            entry = entries[key]
            if entry.type != entry_type:
                self.assertIn(entry.type, total, "listasi ei halutun entry_typen.")

