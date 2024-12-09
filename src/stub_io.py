class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []
    
    def write(self, value):
        self.outputs.append(value)
    
    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""
    def add_input(self, value):
        self.inputs.append(value)
    
    def add_input2(self,value1,value2):
        self.inputs.append(value1)
        self.inputs.append(value2)