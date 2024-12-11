"""
Toteuttaa robotti testin tarvitsemia avainsanoja
"""
from interpreter import Interpreter
from stub_bibtex_manager import StubBibtexManager
from stub_io import StubIO


class RobotLibrary:
    """
    Robot-testit käyttävät tämän luokan tarjoamia metodeja.
    """
    def __init__(self):
        self.test = "testi"
        self.io = StubIO()
        self.data_manager = StubBibtexManager()
        self.interpreter = Interpreter(self.io, self.data_manager)

    def run_application(self):
        """ Käynnistää tulkin """
        self.interpreter.run()

    def populate_data(self):
        """ Lisää kuvaus """
        self.data_manager.populate()

    def input(self, value):
        """ Lisää inputtiin komennon """
        self.io.add_input(value)

    def input_edit(self,value1,value2):
        """ Lisää inputtiin komennot """
        self.io.add_input2(value1,value2)

    def instance_should_contain(self, value):
        """ Tyhmä ensimmäinen testi jotta näkee että testit toimivat """
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
        """ Outputin pitäisi sisältää vähintään merkkijono """
        outputs = self.io.outputs
        if len(outputs) <= 1:
            raise AssertionError(
                f"Output \"{value}\" is not in {self.io.outputs}"
            )
