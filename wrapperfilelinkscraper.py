from perfilelinkscraper import PerFileLinkScraper
from pipelinecomponent import PipelineComponent

class WrapperPerFileLinkScraper (PipelineComponent):
    def __init__ (self, parent, name, data):
        contents = PerFileLinkScraper (parent, name, data)
        pipeline = [contents]
        super ().__init__ (parent, name, data, pipeline)
