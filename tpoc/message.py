# Mesage =
# | Wrapper -- encapsulated
# | Leaf    -- bottom


class Datum:
    def __init__ (self, data):
        self.data = data
    def eval (self):
        return self.data

class Message:
    def __init__ (self, sender, port, data, trail):
        self.sender = Datum (sender)
        self.port = Datum (port)
        self.data = Datum (data)
        self.trail = Datum (trail)

class LeafMessage:
    def __init__ (self, sender, data, trail):
        self.sender = sender
        self.data = data
        self.status = '?'
        self.trail = trail
    def __repr__ (self):
        return "{%s, <%s>,'%s'}" % (self.status, self.port, self.data)

class Message (LeafMessage):
    def __init__ (self, sender, port, data, trail):
        self.sender = sender
        self.port = port
        self.data = data
        self.status = '?'
        self.trail = trail
    def __repr__ (self):
        statusChar = '?'
        if self.status == 'input':
            statusChar = 'i'
        if self.status == 'output':
            statusChar = 'o'
        return "{%s, <%s>,'%s'}" % (statusChar, self.port, self.data)

class InputMessage (Message):
    def __init__ (self, port, data, trail):
        super ().__init__ (self, port, data, trail)
    

class OutputMessage (Message):
    def __init__ (self, port, data, trail):
        super ().__init__ (self, port, data, trail)
    def __repr__ (self):
        return "{o, <%s>,'%s'}" % (self.port, self.data)

        
