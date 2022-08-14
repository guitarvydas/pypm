from pipelinecomponent import PipelineComponent

from mdfilereader import MDFileReader
from linesplitter import LineSplitter
from linkscraper import LinkScraper

class PerFileLinkScraper (PipelineComponent):
    def __init__ (self, parent, name, data):
        step1 = MDFileReader (parent, name)
        step2 = LineSplitter (parent, name)
        step3 = LinkScraper (parent, name)
        pipeline = [step1, step2, step3]
        super ().__init__ (parent, name, data, pipeline)
