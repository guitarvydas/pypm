#!/usr/bin/env python3
import dispatcher
import perfilelinkscraper
disp = dispatcher.Dispatcher ()
top = perfilelinkscraper._perfilelinkscraper (disp, None, '')
top.kickstart ()
disp.dispatch ()
