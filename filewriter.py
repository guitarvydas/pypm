from message import Message
import leaf
class FileWriter (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.filename = ''
        self.fd = None
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            self.filename = message.data
        else:
            if (message.port == 'clear'):
                f = open (self.filename, 'w')
                f.close ()
            else:
                if (message.port == 'append'):
                    f = open (self.filename, 'a')
                    f.write (message.data)
                    f.close ()
                else:
                    raise Exception ('unkown port')
    # def call (self, filename, data):
    #     self.handler ('filename', filename)
    #     self.handler ('clear', True)
    #     self.handler ('append', data)
    #     return ''

# def testFileWriter ():
#     tester = FileWriter (None, 'file writer')
#     tester.handler ('filename', 'test2.txt')
#     tester.handler ('clear', True)
#     tester.handler ('append', 'abc\ndef\nghi\n')
#     print ('file write test done')

# testFileWriter ()
