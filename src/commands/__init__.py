import commands.list as c_list
import commands.add_reference as c_add_reference


command_modules = [c_list, c_add_reference]
commands = {} # Populoituu kun callataan init_commands


def init_commands(parser, subparsers):
    """ Alustaa komennot ja palauttaa ne sanakirjassa. """
    for command_module in command_modules:
        add_command(parser, subparsers, command_module)
    init_default_commands(parser, subparsers)
    return commands


def add_command(parser, subparsers, command_module):
    command_module.add_to_subparsers(parser, subparsers)
    for alias in command_module.aliases:
        commands.update({alias: command_module.execute})


def init_default_commands(parser, subparsers):
    """ TODO: Paloittele """
    parser_help = subparsers.add_parser("help", aliases=["help", "h"], add_help=False, help="usage: help [command]")
    parser_help.add_argument("command", nargs="*", default=[], action="extend")

    # Määritellään custom help-komento
    def help_command(io, data_manager, ns):
        if len(ns.command) == 0:
            parser.print_help(io)
        else:
            command = subparsers.choices.get(ns.command[0])
            if command == None:
                io.write("Unrecognized command.")
                parser.print_help(io)
            else:
                command.print_help(io)

    for alias in ["help", "h"]:
        commands.update({alias: help_command})

    parser_exit = subparsers.add_parser("exit", aliases=["exit", "q"], add_help=False, help="")
    for alias in ["exit", "q"]:
        commands.update({alias: lambda io, data_manager, ns : "exit"})

