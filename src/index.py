from interpreter import Interpreter
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
from commands.index import commands
import signal

# CTRL+C ei kaada ohjelmaa
signal.signal(signal.SIGINT, lambda sig, frame : exit(0))

# TODO: Keksi parempi tiedostonimi
bibtex_file_path = "./test.bib"
data_manager = BibtexManager(bibtex_file_path)
console_io = ConsoleIO()

interpreter = Interpreter(console_io, data_manager, commands)
interpreter.run()
