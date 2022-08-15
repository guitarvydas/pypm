from pipelinecomponent import PipelineComponent

from hello import Hello
from world import World

class HelloWorld (PipelineComponent):
    def __init__ (self, parent, name, data):
        step1 = { 'clss' : Hello, 'name' : f'h[{name}]', 'instanceData' : 'a' }
        step1a = { 'clss' : Hello, 'name' : f'h[{name}]','instanceData' : 'b' }
        step2 = { 'clss': World, 'name' : f'w[{name}]'  ,'instanceData' : 'c' }
        pipeline = [step1, step2, step1a]
        super ().__init__ (parent, name, data, pipeline)
