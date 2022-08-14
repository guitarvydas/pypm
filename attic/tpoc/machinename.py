class MachineName:
    def __init__ (self, machine, state):
        self.machine = machine
        self.state = state
    def __repr__ (self):
        return '[' + self.name () + ']'
    def name (self):
        if typeof (self.state) is String:
            return f'{self.machine}/{self.state}'
        else:
            return f'{self.machine}/{self.state.name ()}'
            
