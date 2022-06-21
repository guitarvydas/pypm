class Link2filename ():
    def __init__ (self):
        self.basename = ''
        self.output = []
    def send (self, portname, data):
        self.output.append ({ 'port': portname, 'data': data })
    def handler (self, port, data):
            if (port == 'basename'):
                self.basename = data + '/'
            else:
                if (port == 'link'):
                    stripped = self.stripLinkBrackets (data)
                    fixedUpForPython = self.fixup (stripped)
                    self.send ('output', self.basename + fixedUpForPython)
    def call (self, basename, link):
        self.handler ('basename', basename)
        self.handler ('link', link)
        return self.outputs2dict ()['output']
    def stripLinkBrackets (self, s):
        strippedPre = s.replace ('[[', '')
        strippedPost = strippedPre.replace (']]', '')
        stripped = strippedPost
        return stripped
    def fixup (self, s):
        result = s.replace (' ', '--').replace ('\n', '')
        return result
    def outputs2dict (self):
        # this could be done more efficiently
        # map all output values into a single dict,
        #    overriding each key/value pair with the most recent value at that key
        # (TODO: should this return a stack of values (alist) for each key instead
        #    of 1 value for each key?)
        resultdict = {}
        for message in self.output:
            resultdict [message ['port']] = message ['data']
        pass
        return resultdict
            
                                
tester = Link2filename ()
tester.handler ('basename', 'xyz')
tester.handler ('link', '[[abc]]')
print (tester.outputs2dict ()['output'])
print (tester.call ('uvw', 'def'))

