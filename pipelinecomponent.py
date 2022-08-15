from message import Message
from state import State
from hsm import HSM

class PipelineComponent (HSM):

    def enter (self):
        super ().enter ()

    def exit (self):
        super ().exit ()

## state idle:
    def enter_IDLE (self):
        self.send ('state', '<idle>', None)

    def exit_IDLE (self):
        self.send ('state', '</idle>', None)

    def handle_IDLE (self, message):
        if message.port == '': 
            self.next ('seq')
            return True
        else:
            return False
        
## state SEQ:
    def instantiatePipeline (self):
        sequence = []
        for descriptor in self.pipeline:
            clss = descriptor ["clss"]
            name = descriptor ["name"]
            data = self.data
            sequence.append (clss (self, name, data))
        return sequence
            
    def enter_SEQ (self):
        self.sequence = self.instantiatePipeline ()
        self.send ('state', '<seq>', None)

    def exit_SEQ (self):
        self.send ('state', '</seq>', None)

    def handle_SEQ (self, message):
        if ('step' == message.port): 
            if 0 == len (self.sequence):
                self.send ('done', True, message)
                self.next ('idle')
            else:
                active = self.sequence.pop (0)
                active.handle (Message (self, '', self.data, message))
                
            return True
        else:
            return False


# overrides unique to the pipeline manager

    def step (self):
        self.handle (Message (self, 'step', True, None))
    
    def isBusy (self):
        # if the pipeline handler is not idle, then it is busy
        return not ('idle' == self._state._name)



## create new instance
    def __init__ (self, parent, instanceName, data, pipeline):
        idle = State (machine=self, name='idle', enter=self.enter_IDLE, exit=self.exit_IDLE, handle=self.handle_IDLE, subMachineClass=None)
        seq = State (machine=self, name='seq', enter=self.enter_SEQ, exit=self.exit_SEQ, handle=self.handle_SEQ, subMachineClass=None)
        stateList = [idle, seq]
        self.data = data
        self.pipeline = pipeline
        super ().__init__ (parent=parent, name=instanceName, 
                           enter=None, exit=None,
                           defaultStateName='idle', states=stateList)
