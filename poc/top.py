#!/usr/bin/env python3
import dispatcher
import linkscraper
disp = dispatcher.Dispatcher ()
top = linkscraper._linkscraper (disp, None, '')
top.kickstart ()
disp.dispatch ()
