
class Interpreter:
    """ Komentotulkki. """
    def __init__(self, io, commands):
        self.io = io
        self.commands = commands

    def executeline(self):
        """ Suorittaa yhden rivin. """
        line = self.io.read("ref-helper> ")
        parts = line.split(" ")
        command = self.get_command(parts)
        if command == None:
            # TODO: Muuta viesti paremmaks ja mahollisesti jopa ulkoista se.
            self.io.write("Tunnistamaton komento. help auttaa")
            return
        # NOTE: Dict => class?
        command["execute"](self.io, parts)
        return 0 # NOTE: Virheen tapahtuessa muuta kuin nolla

    def get_command(self, parts):
        """ Hakee ensimmäistä merkkijonoa vastaavan komennon. """
        for command in self.commands:
            # NOTE: Dict => class?
            for alias in command["alias"]:
                if alias == parts[0]:
                    return command