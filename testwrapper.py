from message import Message

from wrapperfilelinkscraper import WrapperPerFileLinkScraper

data = { 
    'base directory' : '/Users/tarvydas/Dropbox/ps',
    'suffix' : 'md',
    'source filename' : 'test.md', 
    'target filename' : 'out.test.md',
    'md text' : '[[test]] abc def\nghi jkl\nmno [[link2]] pqr\n'
}
wpfls = WrapperPerFileLinkScraper (None, 'wrapper per file link scraper', data, '')
wpfls.inject (Message (None, '', data, None))
print ('injected')
wpfls.run ()
print ('done:')
print (data)
print (wpfls.outputs ())
