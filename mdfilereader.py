from message import Message
import leaf
import re

class MDFileReader (leaf.Leaf):
    def __init__ (self, parent, name): super ().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            if (re.search (r'\.md$', message.data)):
                f = open (message.data, 'r')
                result = f.read ()
                self.send (self, 'text', result, message)
            else:
                self.send (self, 'text', '', message)
    # def call (self, filename):
    #     self.handler (Message (self, 'filename', filename, []))
    #     return self.outputs2dict ()['text']

def testMDFileReader ():
    tester = MDFileReader (None, 'file reader')
    tester.handler (Message (tester, 'filename', 'test.md', []))
    print (tester.outputs2dict ()['text'])

# testMDFileReader ()
