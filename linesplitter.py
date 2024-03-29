import re

from porthandler import PortHandler
from filtercomponent import FilterComponent

class LineSplitter (FilterComponent):
    def __init__ (self, parent, name, data, instanceData):
        super ().__init__ (parent, name, self.handle)
        self.data = data
        self.instanceData = instanceData
        h1 = PortHandler ('md text', self.f1)
        self.handlerFunctions = [h1]

    def f1 (self, message):
        message.data ['md text'].split ('\n')
        
