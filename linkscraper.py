import re

class Linkscraper ():
    def __init__ (self):
        self.output = []
    def send (self, portname, data):
        self.output.append ({ 'port': portname, 'data': data })
    def handler (self, port, data):
        if (port == 'text'):
            text = data.split ('\n')
            result = []
            for line in text:
                matchList = re.findall (r'[^`]\[\[([^]])\]\][^`]', line)
                result = result + matchList
            self.send ('output', result)
    def call (self, text):
        self.handler ('text', text)
        return self.outputs2dict ()['output']
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
            
                                
tester = Linkscraper ()
tester.handler ('text', 'abc[[def]]ghi\n')
print (tester.outputs2dict ()['output'])
#print (tester.call ('uvw', 'def'))

