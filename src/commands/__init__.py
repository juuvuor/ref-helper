"""
commands

Komento-tiedoston tynkäesimerkki:

aliases = ["esim"]

def add_to_subparsers(parser, subparsers):
    parser_esim = subparsers.add_parser("esim", aliases=aliases, add_help=False, help="mitä tää tekee")
    # + muut määrittelyt argumentteihin. Esimerkki list-komento
    # https://docs.python.org/3/library/argparse.html

def execute(io: ConsoleIO, data_manager: BibtexManager, ns: argparse.Namespace):
    pass
    return # Joko ei mitään tai "exit", jolloin interpreter breikkaa while loopista ja ohjelma sulkeutuu.
"""
import commands.list as c_list
import commands.add_reference as c_add_reference
import commands.edit_reference as c_edit_reference
import commands.delete_reference as c_delete_reference


# NOTE: Tänne lisätään komennot, mitkä sitten alustetaan funktiolla init_commands.
command_modules = [
    c_add_reference,
    c_edit_reference,
    c_delete_reference,
    c_list
]


def init_commands(parser, subparsers):
    """ Alustaa komennot ja palauttaa ne sanakirjassa. """
    commands = {}
    for command_module in command_modules:
        add_command(commands, parser, subparsers, command_module)
    init_default_commands(commands, parser, subparsers)
    return commands


def add_command(commands, parser, subparsers, command_module):
    """ Lisää komennot subparserille """
    command_module.add_to_subparsers(parser, subparsers)
    for alias in command_module.aliases:
        commands.update({alias: command_module.execute})


def init_default_commands(commands, parser, subparsers):
    """
    Hoitaa erikoisten komentojen kuten help ja exit alustamisen.
    TODO: Paloittele
    """
    parser_help = subparsers.add_parser(
                                        "help",
                                        aliases=["help", "h"],
                                        add_help=False,
                                        help="usage: help [command]"
                                    )
    parser_help.add_argument("command", nargs="*", default=[], action="extend")

    # Määritellään custom help-komento
    def help_command(io, data_manager, http, ns):
        if len(ns.command) == 0:
            parser.print_help(io)
        else:
            command = subparsers.choices.get(ns.command[0])
            if command is None:
                io.write("Unrecognized command.")
                parser.print_help(io)
            else:
                command.print_help(io)

    for alias in ["help", "h"]:
        commands.update({alias: help_command})

    parser_exit = subparsers.add_parser("exit", aliases=["exit", "q"], add_help=False, help="")
    parser_exit.add_argument("command", nargs="*", default=[], action="extend")
    for alias in ["exit", "q"]:
        commands.update({alias: lambda io, data_manager, http, ns : "exit"})
