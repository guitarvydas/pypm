class STACKofFUNCTIONS:
    def __init__ (self):
        self.stack = []
    def reset (self):
        self.stack = []
    def execAll (self):
        stk = self.stack
        while (stk):
            f = stk.pop ()
            f ()
    def push (self, function):
        self.stack.push (function)
