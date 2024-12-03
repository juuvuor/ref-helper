import commands.list

commands = [
    { "alias": commands.list.alias, "execute": commands.list.execute },
    {
        "alias": ["help", "h"],
        "execute": lambda io, data_manager, args : io.write("Usage: TODO") # TODO
    },
    {
        "alias": ["exit", "q"],
        "execute": lambda io, data_manager, args : exit(0)
    }
]
