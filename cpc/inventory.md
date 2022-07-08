# (copyscript)
## scriptsequencer *sm*
## (generatelinksfile)
### generatefilelinkssequencer *sm*
### (loopbackscraper)
##### (perfilelinkscraper) @ "first"
##### linkcollection
##### loop
##### linktofilename
##### (perfilelinkscraper) "rest"
###### textfilereader
###### omitcomponents
###### omitcodequotes
###### linkscraper
### linestotext
### filewriter
## (copierwrapper)
### mdfilereader
### texttolines
### filterpng
### (manglethencopy) @
### (manglethencopy)
#### prependdir @
#### prependdir
#### mangleformarkua
#### copyfile
## (fixuppngwrapper)
### ls
### prefixfilename
### fixupreferencestopngfiles
### overwritefile
## (fixupmdwrapper)
### ls @
### prefixfilename @
### fixupreferencestomdfiles
### overwritefile @
