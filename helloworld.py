from pipelinecomponent import PipelineComponent

from hello import Hello
from world import World

class HelloWorld (PipelineComponent):
    def __init__ (self, parent, name, data):
        step1 = { 'clss' : Hello, 'name' : f'h[{name}]' }
        step2 = { 'clss': World, 'name' : f'w[{name}]' }
        pipeline = [step1, step2]
        super ().__init__ (parent, name, data, pipeline)
