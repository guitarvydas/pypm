from pipelinecomponent import PipelineComponent

from echo import Echo

class HelloWorld (PipelineComponent):
    def __init__ (self, parent, name, data):
        step1 = { 'clss' : Echo, 'name' : f'h1[{name}]', 'instanceData' : 'hello' }
        step3 = { 'clss' : Echo, 'name' : f'h3[{name}]','instanceData' : 'hello-again' }
        step2 = { 'clss': Echo, 'name' : f'w[{name}]'  ,'instanceData' : 'world' }
        pipeline = [step1, step2, step3]
        super ().__init__ (parent, name, data, pipeline)
