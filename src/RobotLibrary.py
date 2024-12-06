from interpreter import Interpreter
from bibtex_manager import BibtexManager
from commands.index import commands
from stub_io import StubIO
import sys, pdb # debug


class RobotLibrary:
    """
    Robot-testit käyttävät tämän luokan tarjoamia metodeja.
    TODO: BibtexManagerStub
    """
    def __init__(self):
        self.test = "testi"
        self.io = StubIO()
        # TODO: Keksi parempi tiedostonimi jotta voidaan ajaa muualta kuin juuri
        self.bibtex_file_path = "./test.bib"
        self.data_manager = BibtexManager(self.bibtex_file_path)
        self.interpreter = Interpreter(self.io, self.data_manager, commands)

    def run_application(self):
        self.interpreter.run()
    
    def input(self, value):
        self.io.add_input(value)

    def instance_should_contain(self, value):
        testi = self.test

        if not value == testi:
            raise AssertionError(
                f"Output \"{value}\" is not testi"
            )

    def output_should_contain(self, value):
        """ Outputin pitäisi sisältää merkkijono missä tahansa kohdassa. """
        total = "".join(self.io.outputs)
        if not value in total:
            raise AssertionError(
                f"Output \"{value}\" is not in {self.io.outputs}"
            )

    def output_should_contain_atleast(self,value):
        outputs = self.io.outputs
        #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
        if len(outputs) <= 1:
            raise AssertionError(
                f"Output \"{value}\" is not in {self.io.outputs}"
            )

