from message import Message
import leaf
import container
import mdfilereader
import re
class FilterPNGs (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'line'):
            line = message.data
            if (re.search (r'\.png\]\]$', line)):
                self.send (self, 'png', line)
            else:
                self.send (self, 'md', line)
        else:
            raise Exception (f"unrecognized message in FilterPNGs '{message.port}'")


class PNGprintf (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'in'):
            print (f'PNG: {message.data}')
        else:
            raise Exception (f"unrecognized message in FilterPNGs '{message.port}'")

class MDprintf (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'in'):
            print (f'md: {message.data}')
        else:
            raise Exception (f"unrecognized message in FilterPNGs '{message.port}'")


class FilterPNGsTest (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.child_reader = mdfilereader.MDFileReader (None, 'reader')
        self.child_filter = FilterPNGs (None, 'PNG filter')
        self.child_PNGprintf = PNGprintf (None, 'PNG printf')
        self.child_MDprintf = MDprintf (None, 'MD printf')
        self.children = [self.child_reader, self.child_filter, self.child_PNGprintf, self.child_MDprintf]
        self.connections = [
            { 'sender' : self, 'port' : 'filename', 'receivers' : [ { 'receiver' : self.child_reader, 'port' : 'filename' }]},
            { 'sender' : self.child_reader, 'port' : 'text', 'receivers' : [ { 'receiver' : self.child_filter, 'port' : 'text' }]},
            { 'sender' : self.child_filter, 'port' : 'png', 'receivers' : [ { 'receiver' : self.child_PNGprintf, 'port' : 'in' }]},
            { 'sender' : self.child_filter, 'port' : 'md', 'receivers' : [ { 'receiver' : self.child_MDprintf, 'port' : 'in' }]}
        ]
        def handler (self, message):
            super ().handler (message)
            if (message.port == 'filename'):
                self.delegateMessage (message)
                self.route ()
                self.runToCompletion ()
            else:
                raise Exception (f'Unrecognized Port for FilterPNGsTest {message.port}')

def testFilter ():
    tester = FilterPNGsTest (None, 'tester')
    tester.handler (Message (tester, 'filename', 'out.test.md', []))
    print (tester.outputQueueAsList ())

testFilter ()