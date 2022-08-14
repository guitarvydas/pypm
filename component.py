from fifo import FIFO
from message import Message

class Component:
    def __init__ (self, parent, name):
        self._parent = parent
        self._instanceName = name
        self._inputq = FIFO ()
        self._outputq = FIFO ()

    # external to-be-implemented in descendent
    def run (self):
        raise Exception (f'run must be overridden for {self.name}')
    def step (self, message):
        raise Exception (f'step must be overridden for {self.name}')
    def inject (self, message):
        self._inputq.enqueue (message)
    def isBusy (self):
        raise Exception ("isBusy not overridden")

    # external
    def outputs (self):
        # return a dictionary of FIFOs, one FIFO per output port
        resultdict = {}
        for message in self._outputq.asDeque ():
            if (not (message.port in resultdict)):
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        self.clearOutputs ()
        resultdict2 = {}
        for key in resultdict:
            fifo = resultdict [key]
            resultdict2 [key] = fifo.asDeque ()
        return resultdict2
    def isReady (self):
        return (not self._inputq.isEmpty ())
    def name (self):
        parentname = ''
        if self._parent:
            parentname = self._parent.name () + '/'
        return f'{parentname}{self._instanceName}'

    def baseName (self):
        return self._instanceName

    # internal
    def clearOutputs (self):
        self._outputq = FIFO ()

    def enqueueInput (self, message):
        self._inputq.enqueue (message)
        
    def enqueueOutput (self, message):
        self._outputq.enqueue (message)
        

    def dequeueInput (self):
        return self._inputq.dequeue ()
    def dequeueOutput (self):
        return self._outputq.dequeue ()

    def send (self, portname, data, causingMessage):
        if (causingMessage == None):
            trail = [None]
        else:
            trail = [causingMessage, causingMessage.trail]
        m = Message (self, portname, data, trail)
        m.updateState ('output')
        self._outputq.enqueue (m)

