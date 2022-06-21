import leaf
class FileWriter (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.filename = ''
        self.fd = None
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'filename'):
            self.filename = data
        else:
            if (port == 'clear'):
                f = open (self.filename, 'w')
                f.close ()
            else:
                if (port == 'append'):
                    print (f"appending to {self.filename}")
                    f = open (self.filename, 'a')
                    f.write (data)
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
