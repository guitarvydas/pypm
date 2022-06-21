import component
class Leaf (component.Component):
    def __init__ (self, parent, instanceName): super ().__init__ (parent, instanceName)
    def send (self, portname, data):
        self.appendOutputMessage ({ 'port': portname, 'data': data })
    def tick (self):
        if self.ready ():
            message = self.dequeueInputMessage ()
            self.handler (message['port'], message['data'])
        else:
            pass
    def ready (self):
        return len (self.inputq) > 0
    def busy (self):
        return False
    def outputs2dict (self):
        # this could be done more efficiently
        # map all output values into a single dict,
        #    overriding each key/value pair with the most recent value at that key
        # (TODO: should this return a stack of values (alist) for each key instead
        #    of 1 value for each key?)
        resultdict = {}
        for message in self.outputQueueAsList ():
            resultdict [message ['port']] = message ['data']
        pass
        return resultdict

