from interpreter import Interpreter
from console_io import ConsoleIO

console_io = ConsoleIO()
# NOTE: Dict => class?
commands = [
    {
        "alias": ["test"],
        "execute": lambda io, args : io.write("test: " + str(args))
    },
    {
        "alias": ["help", "h"],
        "execute": lambda io, args : io.write("Usage: TODO") # TODO
    },
    {
        "alias": ["exit", "q"],
        "execute": lambda io, args : exit(0)
    }
]

i = Interpreter(console_io, commands)
while True:
    i.executeline()
