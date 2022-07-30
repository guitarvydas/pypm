# Message =
# | Sender Port Message State Trail -- encapsulated
# | Base                            -- bottom


class BaseMessage:
    def __init__ (self, data):
        self.data = data
    def value (self):
        return self.data
    def __repr__ (self):
        return "%s" % (self.data)

class Message (BaseMessage):
    def __init__ (self, sender, port, data, trail):
        super ().__init__ (data)
        self.sender = sender
        self.port = port
        self.trail = trail
        self.state = '?'
    def __repr__ (self):
        return "{%s, %s, '%s','%s'}" % (self.state, self.sender.name,
                                        self.port, super ().__repr__)

    def updateState (self, newState):
        if (newState == 'input'):
            self.state = 'input'
        elif (newState == 'output'):
            self.state = 'output'
        else:
            raise Exception ("illegal state for Message {newState}")
