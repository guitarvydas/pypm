#!/usr/bin/env python3
import dispatcher
import re
import perfilelinkscraper
disp = dispatcher.Dispatcher ()
top = perfilelinkscraper._perfilelinkscraper (disp, None, '')
top.kickstart ()
disp.dispatch ()
