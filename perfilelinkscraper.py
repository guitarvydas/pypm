from pipelinecomponent import PipelineComponent

class PerFileLinkScraper (PipelineComponent):
    def __init__ (self, parent, name):
        data = { 
            'base directory' : '/Users/tarvydas/Dropbox/ps',
            'suffix' : 'md',
            'source filename' : 'test2.md', 
            'target filename' : 'out.test.md',
        }
        step1 = MDFileReader (parent, name)
        step2 = LineSplitter (parent, name)
        step3 = LinkScraper (parent, name)
        pipeline = [step1, step2, step3]
        super ().__init__ (parent, name, data, pipeline)
