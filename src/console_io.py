class ConsoleIO:
    """ Injektoitava IO luokka. """
    def write(self, value):
        """ Kirjoittaa consoleen rivin. """
        print(value)

    def read(self, prompt):
        """ Lukee consolesta rivin. """
        return input(prompt)