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
            self.sequence = self.pipeline
            self.next ('seq')
            return True
        else:
            return False
        
## state SEQ:
    def enter_SEQ (self):
        self.send ('state', '<seq>', None)

    def exit_SEQ (self):
        self.send ('state', '</seq>', None)

    def handle_SEQ (self, message):
        if message.port == 'step': 
            if 0 == len (self.sequence):
                self.send (self, 'done', true, message)
                self.next ('idle')
            else:
                active = self.sequence.pop (0)
                active.handle (Message ('', self.data, message))
                
            return True
        else:
            return False


# overrides unique to the pipeline manager

    def step (self):
        self.handle ('step')
    
    def isBusy (self):
        # if the pipeline handler is not idle, then it is busy
        return not ('idle' == self.state.name)



## create new instance
    def __init__ (self, parent, instanceName, data):
        idle = State (machine=self, name='idle', enter=self.enter_IDLE, exit=self.exit_IDLE, handle=self.handle_IDLE, subMachineClass=None)
        seq = State (machine=self, name='seq', enter=self.enter_SEQ, exit=self.exit_SEQ, handle=self.handle_SEQ, subMachineClass=None)
        stateList = [idle, seq]
        super ().__init__ (parent, instanceName, 
                           enter=None, exit=None,
                           defaultStateName='idle', states=stateList,
                           data)
