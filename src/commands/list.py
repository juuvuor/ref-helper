
alias = ["list", "l"]
def execute(io, data_manager, args):
    """ Listaa referenssit. """
    # TODO: args avulla voi määritellä filter/sort
    data = data_manager.get_data()
    # print(data)
    for entry in data.entries:
        io.write(data.entries[entry].to_string("bibtex"))
