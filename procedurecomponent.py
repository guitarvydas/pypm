from hsm import HSM
from state import State

class ProcedureComponent (HSM):
    def Noop (self):
        pass

    def defaultHandler (self, message):
        self.handler (message)
        
    def __init__ (self, parent, instanceName, handler):
        self.handler = handler
        defaultState = State (machine=self, name='default', enter=self.Noop, exit=self.Noop, handle=self.defaultHandler, subMachineClass=None)
        stateList = [defaultState]
        super ().__init__ (parent, instanceName, 
                           enter=None, exit=None,
                           defaultStateName='default', states=stateList)
