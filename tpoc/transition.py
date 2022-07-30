class Transition:
    def __init__ (self, state, port, function, nextStateName, nextStateEntryFunction):
        self.state = state
        self.port = port
        self.function = function
        self.nextStateName = nextStateName
        self.nextStateEntryFunction = nextStateEntryFunction
    def isNoChange (self):
        return (self.next == None or self.next = '.')
