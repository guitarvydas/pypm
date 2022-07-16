class Message:
    def __init__ (self, sender, port, data, trail):
        self.sender = sender
        self.port = port
        self.data = data
        self.status = 'deferred'
        if (isinstance (trail,list) and len(trail) == 0):
            self.trail = []
        elif isinstance (trail, list):
            self.trail = trail
        else:   
            raise Exception ("internal error in Message - trail is not empty nor a list")
            self.trail = trail


    def newCopy (self):
        m = Message (self.sender, self.port, self.data, self.trail)
        return m
    
    def __repr__ (self):
        # return "{<%s>,...}" % (self.port)
        return "{<%s>,'%s'}" % (self.port, self.data)
