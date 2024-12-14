"""
Alustaa ja käynnistää
"""
import signal
from interpreter import Interpreter
from console_io import ConsoleIO
from bibtex_manager import BibtexManager
import http_util

# CTRL+C ei kaada ohjelmaa
signal.signal(signal.SIGINT, lambda sig, frame : exit(0))

# TODO: Keksi parempi tiedostonimi
BIBTEX_FILE_PATH = "./test.bib"
data_manager = BibtexManager(BIBTEX_FILE_PATH)
console_io = ConsoleIO()
http = http_util
interpreter = Interpreter(console_io, data_manager, http)
interpreter.run()
