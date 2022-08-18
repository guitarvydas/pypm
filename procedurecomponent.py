from component import Component

class ProcedureComponent (Component):
    def __init__ (self, parent, name, handlerFunctions, data, instanceData):
        super ().__init__ (parent, name)
        self.data = data
        self.instanceData = instanceData
        self.handlerFunctions = handlerFunctions
        self.subLayer = None
        
