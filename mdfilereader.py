import re
from procedurecomponent import ProcedureComponent

class MDFileReader (ProcedureComponent):
    def f1 (self, message):
        data = message.data
        if (re.search (r'\.md$', data ["source filename"])):
            f = open (data ["source filename"], 'r')
            result = f.read ()
            data ["md text"] = result

    def __init__ (self, parent, name, data, instanceData):
        super ().__init__ (parent, name, self.handle)
        self.data = data
        self.instanceData = instanceData
        h1 = PortHandler ('filename', self.f1)
        self.handlerFunctions = [h1]
