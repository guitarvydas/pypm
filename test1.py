from message import Message

from perfilelinkscraper import PerFileLinkScraper

data = { 
    'base directory' : '/Users/tarvydas/Dropbox/ps',
    'suffix' : 'md',
    'source filename' : 'test.md', 
    'target filename' : 'out.test.md',
    'md text' : '[[test]] abc def\nghi jkl\nmno [[link2]] pqr\n'
}
pfls = PerFileLinkScraper (None, 'per file link scraper', data)
pfls.inject (Message (None, '', data, None))
print ('injected')
pfls.run ()
print ('done:')
print (data ["[links]"])
