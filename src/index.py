from interpreter import Interpreter
from console_io import ConsoleIO
from bibtex_manager import BibtexManager


# TODO: Keksi parempi nimi
bibtex_file_path = "./test.bib"
data_manager = BibtexManager(bibtex_file_path)

console_io = ConsoleIO()


# NOTE: Dict => class?
commands = [
    {
        "alias": ["test"],
        "execute": lambda io, data_manager, args : io.write("test: " + str(args) + data_manager.get_data().to_string("bibtex"))
    },
    {
        "alias": ["help", "h"],
        "execute": lambda io, data_manager, args : io.write("Usage: TODO") # TODO
    },
    {
        "alias": ["exit", "q"],
        "execute": lambda io, data_manager, args : exit(0)
    }
]

i = Interpreter(console_io, data_manager, commands)
while True:
    i.executeline()
