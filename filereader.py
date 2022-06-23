from message import Message
import leaf
class FileReader (leaf.Leaf):
    def __init__ (self, parent, name): super ().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            f = open (message.data, 'r')
            result = f.read ()
            self.send (self, 'text', result)
    # def call (self, filename):
    #     self.handler (Message (self, 'filename', filename))
    #     return self.outputs2dict ()['text']

def testFileHandler ():
    tester = FileReader (None, 'file reader')
    tester.handler (Message (tester, 'filename', 'test.txt'))
    print (tester.outputs2dict ()['text'])

testFileHandler ()
