class StubIO:
    """ Toteuttaa testeille tyngän """
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        """ Lisää outputtiin """
        self.outputs.append(value)

    def read(self, prompt):
        """ Lukee inputin """
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def add_input(self, value):
        """ Lisää inputtiin """
        self.inputs.append(value)
