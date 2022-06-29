from message import Message
import leaf
import shutil

class CopyFile (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.src = None
        self.dest = None
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'src'):
            self.src = message.data
            self.dataflowConditionalAction ()
        elif (message.port == 'dest'):
            self.dest = message.data
            self.dataflowConditionalAction ()
        else:
            raise Exception (f"unrecognized message in CopyFile '{message.port}'")

    def dataflowCopyConditionalAction ():
        # trigger copy action only if both src and dest have been received
        if (self.src and self.dest):
            shutil.copyfile(self.src, self.dest)
            # clear both inputs
            self.src = None
            self.dest = None
