from message import Message
class Component:
    def __init__ (self, parent, instanceName):
        self.parent = parent
        self.name = instanceName
        self.inputq = []
        self.outputq = []
        self.debugTick = False
        self.debugHandler = True
        self.debugInput = False
        self.debugOutput = False
    def send (self, sender, portname, data, cause):
        previous_trail = cause.trail
        trail = [cause, previous_trail]
        self.appendOutputMessage (Message (sender, portname, data, trail))
    def outputs2dict (self):
        # this could be done more efficiently
        # map all output values into a single dict,
        #    overriding each key/value pair with the most recent value at that key
        # (TODO: should this return a stack of values (alist) for each key instead
        #    of 1 value for each key?)
        resultdict = {}
        for message in self.outputQueueAsList ():
            resultdict [message.port] = message.data
        self.resetOutputQueue ()
        return resultdict
    def inputQueueNotEmpty (self):
        return len (self.inputq) > 0
    def outputQueueNotEmpty (self):
        return len (self.outputq) > 0
    def appendInputMessage (self, message):
        if (self.debugInput):
            print (f"  append input '{self.name}' /{message.port}/")
        m = Message (message.sender, message.port, message.data, message.trail)
        self.inputq.append (m)
    def appendOutputMessage (self, message):
        if (self.debugOutput):
            print (f"  append output '{self.name}' /{message.port}/")
        m = Message (self, message.port, message.data, message.trail)
        self.outputq.append (m)
    def dequeueInputMessage (self):
        return self.inputq.pop (0)
    def outputQueueAsList (self):
        return self.outputq
    def resetOutputQueue (self):
        self.outputq = []
    def handler (self, message):
        if (self.debugHandler):
            print (f"handler '{self.name}' '⟨{message.port}⟩'")
        pass
    def ready (self):
        return self.inputQueueNotEmpty ()
    def route (self):
        pass
    def tick (self):
        if (self.debugTick):
            print (f'   tick {self.name}')
        pass
