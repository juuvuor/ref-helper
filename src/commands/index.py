import commands.list

commands = [
    { "alias": commands.list.alias, "execute": commands.list.execute },
    {
        "alias": ["help", "h"],
        "execute": lambda io, data_manager, args : io.write("Usage: TODO") # TODO
    },
    {
        "alias": ["exit", "q"],
        "execute": lambda io, data_manager, args : (data_manager.write(), exit(0))
    },
    {
        "alias": ["add_reference", "add"],
        "execute": lambda io, data_manager, args : data_manager.prompt_for_reference()
    }
]
