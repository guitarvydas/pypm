from message import Message, OutputMessage
from fifo import FIFO
from stackoffunctions import STACKofFUNCTIONS

class Component:
    def __init__ (self, parent, instanceName):
        self.parent = parent
        self.instanceName = instanceName
        self.inputq = FIFO ()
        self.outputq = FIFO ()
        self.state = '?'
        self.exitStack = STACKofFUNCTIONS ()
        self.debugStep = False
        self.debugReset = True

    # external
    def step (self):
        ...
    def reset (self):
        for ...
    def inject (self, message):
        self.inputq.enqueue (message)
    def outputs (self):
        # return a dictionary of FIFOs, one FIFO per output port
        resultdict = {}
        for message in self.outputq ():
            if None == resultdict [message.port]:
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        self.outputq = FIFO () # discard outputq
        return resultdict
    def isBusy (self):
        raise Exception ("isBusy not overridden")
    def on (self, message, transitionList):
        for transition in transitionList:
            if (self.state == transition.state and message.port == transition.port):
                transition.function ()
                if transition.isNoChange ():
                    pass
                else:
                    self.updateState (transition.state)
                return
        self.handleNonMatchingMessage (message)
    def name (self):
        if (None == self.parent):
            return self.instanceName
        else:
            return f'{self.parent.name}/{self.instanceName}'
    def updateState (self, newState, entryFunction):
        self.exitStack.execAll ()
        self.exitStack.reset ()
        entryFunction ()
        self.state = newState


    # internal
    def dequeueInput (self):
        return self.inputq.pop ()
    def send (self, portname, data, causingMessage):
        trail = [causingMessage, causingMessage.trail]
        self.outputq.enqueue (Message (self, portname, data, trail))
        self.outputq.updateState ('output')
    def handleNonMatchingMessage (self, message):
        # normal: just drop the message
        # but, in this POC, raise an error
        print ()
        print (f'unhandled message {message} for {self.hierarchicalName ()}')
        exit ()
    def enqueueExit (self, function):
        self.exitStack.push (function)
