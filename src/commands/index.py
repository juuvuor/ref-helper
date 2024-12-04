import commands.list as c_list
import commands.add_reference as c_add_reference

commands = [
    { "alias": c_list.alias, "execute": c_list.execute },
    { "alias": c_add_reference.alias, "execute": c_add_reference.execute },
    {
        "alias": ["help", "h"],
        "execute": lambda io, data_manager, args : io.write("Usage: TODO") # TODO
    },
    {
        "alias": ["exit", "q"],
        "execute": lambda io, data_manager, args : (data_manager.write(), exit(0))
    }
]
