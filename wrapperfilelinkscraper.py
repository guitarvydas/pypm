from perfilelinkscraper import PerFileLinkScraper
from pipelinecomponent import PipelineComponent

class WrapperPerFileLinkScraper (PipelineComponent):
    def __init__ (self, parent, name, data, instanceData):
        contents = { 'clss': PerFileLinkScraper, 'name': name }
        pipeline = [contents]
        super ().__init__ (parent, name, data, pipeline)
