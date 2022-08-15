from pipelinecomponent import PipelineComponent

from mdfilereader import MDFileReader
from linesplitter import LineSplitter
from linkscraper import LinkScraper

class PerFileLinkScraper (PipelineComponent):
    def __init__ (self, parent, name, data):
        step1 = { 'clss' : MDFileReader, 'name' : f'markdown file reader[{name}]' }
        step2 = { 'clss': LineSplitter, 'name' : f'line splitter[{name}]' }
        step3 = { 'clss' : LinkScraper, 'name' : f'link scraper[{name}]' }
        pipeline = [step1, step2, step3]
        super ().__init__ (parent, name, data, pipeline)
