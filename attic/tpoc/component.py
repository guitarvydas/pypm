from message import Message, OutputMessage
from fifo import FIFO
from stackoffunctions import STACKofFUNCTIONS

defaultStateName = '?'

class Component:
    def __init__ (self, parent, instanceName, initialState):
        self.parent = parent
        self.instanceName = instanceName
        self.inputq = FIFO ()
        self.outputq = FIFO ()
        self.state = initialState
        self.initialState.fenter ()
        self.exitStack = STACKofFUNCTIONS ()
        self.exitState.push (initialState.fexit)
        self.defaultEntry = defaultEntry
        self.defaultExit = defaultExit
        self.defaultEntry ()

    # external
    def step (self, message):
        self.state.fhandler (message)
    def reset (self):
        self.updateState (self, '', self.defaultEntry)
    def inject (self, message):
        self.inputq.enqueue (message)
    def outputs (self):
        # return a dictionary of FIFOs, one FIFO per output port
        self.exitDefault ()
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
            if (self.state.name == transition.state.name):
                and message.port == transition.port):
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
    def updateState (self, newState, entryFunction, exitFunction):
        # jump "across" to another state,
        # exit current state and all sub-states in LIFO order (exit deepest children first)
        self.exitStack.execAll ()
        self.exitStack.reset ()
        entryFunction ()
        self.exitStack.push (exitFunction)
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
    def exitDefault (self):
        self.defaultExit ()
    def dive (self, newState, entryFunction, exitFunction):
        # dive into sub-machine, do not exit current state(s)
        entryFunction ()
        self.exitStack.push (exitFunction)
        self.state = newState
