from message import Message

from linesplitter import LineSplitter

lines = LineSplitter (None, 'line splitter')
data = { 
    'base directory' : '/Users/tarvydas/Dropbox/ps',
    'suffix' : 'md',
    'source filename' : 'test2.md', 
    'target filename' : 'out.test.md',
    'md text' : '[[test]] abc def\nghi jkl\nmno [[link2]] pqr\n'
}
lines.inject (Message (None, 'begin', data, None))
print ('injected')
lines.run ()
print ('done:')
print (data)
