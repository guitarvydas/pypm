from message import Message
class Component:
    def __init__ (self, parent, instanceName):
        self.parent = parent
        self.name = instanceName
        self.inputq = []
        self.outputq = []
        self.state = 'default'
        self.exitStack = [self.EmptyExit]
        self.debugStep = False
        self.debugReset = True
    def send (self, portname, data, causingMessage):
        trail = [causingMessage, causingMessage.trail]
        self.outputQueue.append (OutputMessage (self, portname, data, trail))
    def forEachOutput (self, func):
    def outputs (self):
        # this could be done more efficiently
        # map all output values into a single dict,
        #    overriding each key/value pair with the most recent value at that key
        # (TODO: should this return a stack of values (alist) for each key instead
        #    of 1 value for each key?)
        resultdict = {}
        for message in self.outputa ():
            resultdict [message.port] = message.data
        self.resetOutputQueue ()
        return resultdict
