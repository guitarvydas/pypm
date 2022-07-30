from doctest import OutputChecker
from message import Message, OutputMessage
from fifo import FIFO
class Component:
    def __init__ (self, parent, instanceName):
        self.parent = parent
        self.name = instanceName
        self.inputq = FIFO ()
        self.outputq = FIFO ()
        self.state = 'default'
        self.exitStack = [self.EmptyExit]
        self.debugStep = False
        self.debugReset = True
    def send (self, portname, data, causingMessage):
        trail = [causingMessage, causingMessage.trail]
        self.outputQueue.append (OutputMessage (self, portname, data, trail))
    def outputs (self):
        # this could be done more efficiently
        # map all output values into a single dict,
        #    overriding each key/value pair with the most recent value at that key
        # (TODO: should this return a stack of values (alist) for each key instead
        #    of 1 value for each key?)
        resultdict = {}
        for message in self.outputq ():
            resultdict [message.port] = message.data
        self.outputq = FIFO ()
        return resultdict

    def dequeueInput (self):
        return self.inputq.dequeue ()
    
    def inject (self, message):
        self.inputq.enqueue (message)

    def EmptyEntry (self):
        pass
    def EmptyExit (self):
        pass

    def on (self, message, listOfConditions):
        port = message.port
        for cond in listOfConditions:
            state = cond[0]
            port = cond [1]
            handler = cond [2]
            if self.state == state:
                if message.port == port:
                    handler (self, message)
            else:
                self.handleNonMatchingMessage (message)

    # must be implemented...
    def reset (self):
        raise "reset not implemented"
    def step (self):
        raise "step not implemented"

    
    # internal
    def inputReadyP (self):
        return self.inputq.len ()

    def hierarchicalName (self):
        myname = f'❲{self.name}❳'
        if self.parent == None:
            return myname
        else:
            return f'{self.parent.hierarchicalName ()}/{myname}'

    def handleNonMatchingMessage (self, message):
        # normal: just drop the message
        # but, in this POC, raise an error
        print ()
        print (f'unhandled message {message} for {self.hierarchicalName ()}')
        exit ()
