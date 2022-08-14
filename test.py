from mdfilereader import MDFileReader
from message import Message

mdfr = MDFileReader (None, 'markdown file reader')
data = { 
    'base directory' : '/Users/tarvydas/Dropbox/ps',
    'suffix' : 'md',
    'source filename' : 'test.md', 
    'target filename' : 'out.test.md'
}
mdfr.inject (Message (None, 'begin', data, None))
print ('injected')
mdfr.run ()
print ('done:')
print (data)
