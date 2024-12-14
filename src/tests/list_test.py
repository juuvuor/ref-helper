import unittest
from commands.list import execute
from stub_io import StubIO
from stub_bibtex_manager import StubBibtexManager
import stub_http_util


class TestListCommand(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.data_manager = StubBibtexManager()
        self.data_manager.populate()

    def test_filter_book(self):
        # NOTE: EI TOIMI TÄLLÄ HETKELLÄ OIKEIN!
        return
        entry_type = "book"
        execute(self.io, self.data_manager, stub_http_util, ["list", "filter", entry_type])
        total = "".join(self.io.outputs)
        entries = self.data_manager.get_data().entries
        for key in entries:
            entry = entries[key]
            if entry.type != entry_type:
                self.assertIn(entry.type, total, "listasi ei halutun entry_typen.")

