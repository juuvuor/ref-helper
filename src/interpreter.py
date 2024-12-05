import re


class Interpreter:
    """ Komentotulkki. """
    def __init__(self, io, data_manager, commands):
        self.io = io
        self.data_manager = data_manager
        self.commands = commands

    def executeline(self):
        """ Suorittaa yhden rivin. """
        line = self.io.read("ref-helper> ")
        args = self.to_args(line)
        command = self.get_command(args)
        if command == None:
            # TODO: Muuta viesti paremmaks ja mahollisesti jopa ulkoista se.
            self.io.write("Tunnistamaton komento. help auttaa")
            return 0
        command["execute"](self.io, self.data_manager, args)
        return 0 # NOTE: Virheen tapahtuessa muuta kuin nolla
        # Käytännössähän tämä on turha, koska virhe catchataan metodin ulkopuolella ja sitä kautta saadaan detailed error message printattua
    
    def to_args(self, str: str):
        """
        Jakaa merkkijonon osiin huomioiden lainausmerkit.
        src: https://stackoverflow.com/questions/554013/regular-expression-to-split-on-spaces-unless-in-quotes
        """
        return re.findall('\\w+|"[\\w\\s]*"', str)

    def get_command(self, args):
        """ Hakee ensimmäistä merkkijonoa vastaavan komennon. """
        for command in self.commands:
            for alias in command["alias"]:
                if alias == args[0]:
                    return command