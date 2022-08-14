from message import Message, InputMessage
from mdfilereader0d import MD__File__Reader

def mdfilereader (filename):
    reader = MD__File__Reader (None, 'markdown file reader')
    reader.inject (reader.InputMessage ('filename', filename, None))
    reader.step ()
    return reader.outputs

x = mdfilereader ('test.txt')
print (x)

