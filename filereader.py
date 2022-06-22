import leaf
class FileReader (leaf.Leaf):
    def __init__ (self, parent, name): super ().__init__ (parent, name)
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'filename'):
            f = open (data, 'r')
            result = f.read ()
            self.send ('text', result)
    # def call (self, filename):
    #     self.handler ('filename', filename)
    #     return self.outputs2dict ()['text']

# def testFileHandler ():
#     tester = FileReader (None, 'file reader')
#     tester.handler ('filename', 'test.txt')
#     print (tester.outputs2dict ()['text'])
