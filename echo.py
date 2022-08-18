from porthandler import PortHandler
from procedurecomponent import ProcedureComponent

class Echo (ProcedureComponent):
    def f1 (self, message):
        self.send ('stdout', self.instanceData, message)

    def __init__ (self, parent, name, data, instanceData):
        h1 = PortHandler ('', self.f1)
        super ().__init__ (parent, name, handlerFunctions=[h1], data=data, instanceData = instanceData)
