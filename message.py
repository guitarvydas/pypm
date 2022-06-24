class Message:
    def __init__ (self, sender, port, data):
        self.sender = sender
        self.port = port
        self.data = data

    def newCopy (self):
        m = Message (self.sender, self.port, self.data)
        return m
    
    def __repr__ (self):
        # return "{<%s>,...}" % (self.port)
        return "{<%s>,'%s'}" % (self.port, self.data)
