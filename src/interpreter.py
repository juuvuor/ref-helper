import re
import argparse
import commands
#import sys, pdb # debug


latest_error_message = "" 
class CustomArgumentParser(argparse.ArgumentParser):
    """ Customoitu argument parser, koska error printataan muuten stderr. """
    def error(self, message):
        global latest_error_message
        latest_error_message = message
        raise Exception(message)


class Interpreter:
    """
    Komentotulkki.
    Tulostusten pitäisi tulla annettuun io-luokkaan, mutta voi olla,
    että argparse jossain edge-tapauksessa printtaa stdout tai stderr..
    bug reporttia, niin korjataan.
    """
    def __init__(self, io, data_manager):
        self.io = io
        self.data_manager = data_manager
        self.parser = CustomArgumentParser(prog="", add_help=False)
        self.subparsers = self.parser.add_subparsers(metavar="<command>", dest="command_name")
        self.commands = commands.init_commands(self.parser, self.subparsers)

    def run(self):
        while True:
            #pdb.Pdb(stdout=sys.__stdout__).set_trace() # debug
            try:
                result = self.executeline()
                if result == "exit":
                    break
            except Exception as e:
                if hasattr(e, "message"):
                    print(f"Error: {e.message}")
                else:
                    print(f"Error: {e}")

    def executeline(self):
        """ Suorittaa yhden rivin. """
        line = self.io.read("ref-helper> ")
        parts = Interpreter.str_to_args(line)

        try:
            parsed = self.parser.parse_args(parts)
        except Exception or SystemExit:
            parsed = parts

        # parsed joko argparse.Namespace tai list[str]
        if isinstance(parsed, list):
            command_name = parsed[0] if len(parsed) > 0 else ""
        else:
            command_name = parsed.command_name or ""

        command = self.commands.get(command_name)
        if command == None:
            if len(command_name) > 0:
                self.io.write("Unrecognized command.")
            self.parser.print_help(self.io)
        else:
            if isinstance(parsed, argparse.Namespace):
                return command(self.io, self.data_manager, parsed)
            else:
                self.io.write(command_name + ": error: " + latest_error_message)
                self.subparsers.choices.get(command_name).print_help(self.io)

    @staticmethod
    def str_to_args(str: str):
        """ Jakaa merkkijonon osiin huomioiden lainausmerkit. """
        # Säännöllinen lauseke matchaa kaiken non-whitespacen ja huomioi lainausmerkit.
        result = re.findall(r'".*"|\S+', str)
        # Säännöllinen lauseke jättää lainausmerkit ja tämä poistaa ne.
        result = list(map(lambda arg : arg[1:-1] if arg[0] == '"' and arg[-1] == '"' else arg, result))
        return result
