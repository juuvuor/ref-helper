import re
import sys, pdb # debug


class Interpreter:
    """
    Komentotulkki.
    NOTE: On olemassa moduuli nimeltä argparse  https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
    Sillä saa suoraan parsettua argumentit ja komennot voi hyödyntää sen tarjoamaa rajapintaa.
    """
    def __init__(self, io, data_manager, commands):
        self.io = io
        self.data_manager = data_manager
        self.commands = commands

    def run(self):
        while True:
            #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
            try:
                result = self.executeline()
                if result == "exit":
                    break
                # Testit toimivat, koska ne hyödyntävät tätä statementtia, mikä oli alkuunsakin bugi.
                #if result == None:
                #    break
            except Exception as e:
                if hasattr(e, "message"):
                    print(f"Error: {e.message}")
                else:
                    print(f"Error: {e}")

    def executeline(self):
        """ Suorittaa yhden rivin. """
        line = self.io.read("ref-helper> ")
        parts = Interpreter.to_args(line)
        command = self.get_command(parts)
        if command == None:
            # TODO: Muuta viesti paremmaks ja mahollisesti jopa ulkoista se.
            self.io.write("Tunnistamaton komento. help auttaa")
            return
        return command["execute"](self.io, self.data_manager, parts)

    @staticmethod
    def to_args(str: str):
        """
        Jakaa merkkijonon osiin huomioiden lainausmerkit.
        NOTE: Tällä hetkellä ei ota huomioon escapettuja lainausmerkkejä.
        src: https://stackoverflow.com/questions/554013/regular-expression-to-split-on-spaces-unless-in-quotes
        """
        return re.findall(r'\w+|"[\w\s]*"', str)

    def get_command(self, parts):
        """ Hakee ensimmäistä merkkijonoa vastaavan komennon. """
        for command in self.commands:
            for alias in command["alias"]:
                if alias == parts[0]:
                    return command