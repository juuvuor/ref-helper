import unittest
import stub_http_util
import argparse
from commands.delete_reference import execute
from interpreter import CustomArgumentParser
from stub_io import StubIO
from stub_bibtex_manager import StubBibtexManager


class TestDeleteCommand(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.io.add_input("k")
        self.data_manager = StubBibtexManager()
        self.data_manager.populate()

    def test_delete_book_martin(self):
        poistettava_referenssi = "Martin09"
        args = argparse.Namespace()
        # Namespace(command_name='d', delete_key='VPL11')
        args.command_name = "d"
        args.delete_key = poistettava_referenssi
        execute(self.io, self.data_manager, stub_http_util, args)

        entries = self.data_manager.get_data().entries
        for key in entries:
            if key == poistettava_referenssi:
                self.fail("Avain löytyi poiston jälkeenkin")
        self.assertTrue(True)
