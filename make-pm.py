# clear $output/manuscript
# clear $output/resources

# for each line in script:
#     copy $line.md $output.manuscript
#     scan $line.md for .png files and
#         'copy them to $output/resources'
#     scan $line.md for .md files and
#         'copy them to $output/manuscript'
#         'add them $stack'

# repeat above for each line in stack
#     'if any files were copyd, keep repeating, else quit'



input = '../ps'
script = input + '/Pattern Matching.md'
output = '.'
stack = './stack'
refs = './refs'
missing  =  './missing'

# clear $output/manuscript
# clear $output/resources

import os
import glob
import shutil
import tempfile
import re

manuscript = output + '/' + "manuscript"
resources = manuscript + '/' + "resources"


# for each line in script:
#     copy $line.md $output.manuscript
#     scan $line.md for .png files and
#         'copy them to $output/resources'
#     scan $line.md for .md files and
#         'copy them to $output/manuscript'
#         'add them $stack'

def appendToStack (s):
    f = open (stack, 'a')
    f.write (s)
    f.write ('\n')
    f.close ()
    
def mangleInputFilename (s):
    return s.replace ('\n', '').replace ('[[', '').replace (']]', '').strip ().lower ()

def markua (s):
    return s.replace ('\n', '').strip ().lower ().replace (' ', '--')

def reformatNameForLeanPub (s):
    return markua (mangleInputFilename (s))

def tagAndCopyFile (srcfname, destfname, tag, filter):
    with open (destfname, 'w') as outf:
        with open (srcfname) as inf:
            outf.write (tag)
            for line in inf:
                outf.write (filter (line))

def makeTag (f):
    return  '{id: ' + markua (mangleInputFilename (f)) + '}\n'

## filters

def identity (line):
    return line

def convertObsidianTagsToMarkuaTags (line):
    m = re.search (r'[^`]\[\[([^]]*.png)\]\][^`]', line)
    if (m):
        pngname = m.group (1)
        s = re.sub (r'[^`]\[\[([^]]*)\]\]', f'![{m.group(1)}](resources/' + markua  (pngname) + ')', line)
        return s
    else:
        m = re.search (r'^\[\[([^]]*)\]\][^`]', line)
        if (m):
            s = re.sub (r'\[\[([^]]*)\]\]', f'[{m.group(1)}](#' + markua (m.group(1)) + ')', line)
            return  s
        else:
            m = re.search (r'[^`]\[\[([^]]*)\]\][^`]', line)
            if (m):
                s = re.sub (r'\[\[([^]]*)\]\]', f'[{m.group(1)}](#' + markua (m.group(1)) + ')', line)
                return  s
            else:
                return line

def memo (name):
    with open (refs, 'a') as reffile:
        print (name, file=reffile)

def memoRefs (line):
    m = re.search (r'[^`]\[\[([^]]*.png)\]\][^`]', line)
    if (m):
        pngname = m.group (1)
        newname = resources + '/' + reformatNameForLeanPub (pngname)
        memo (newname)
    else:
        m = re.search (r'^\[\[([^]]*)\]\][^`]', line)
        if (m):
            pngname = m.group (1)
            newname = manuscript + '/' + reformatNameForLeanPub (pngname)  + '.md'
            memo (newname)
        else:
            m = re.search (r'[^`]\[\[([^]]*)\]\][^`]', line)
            if (m):
                pngname = m.group (1)
                newname = manuscript + '/' + reformatNameForLeanPub (pngname)  + '.md'
                memo (newname)
            else:
                pass

def copyPngFile (line):
    m = re.search (r'[^`]\[\[([^]]*.png)\]\][^`]', line)
    if (m):
        pngname = m.group (1)
        newname = reformatNameForLeanPub (pngname)
        tag = makeTag (pngname)
        shutil.copy (input + '/' + pngname, resources + '/' + newname)
#        tagAndCopyFile (input + '/' + pngname, resources + '/' + newname)
    else:
        pass

stateInQuote = False

def filterObsidianLine (line):
    global stateInQuote

    if (line.strip () == '```'):
        if (stateInQuote):
            stateInQuote = False
        else:
            stateInQuote = True
    else:
        pass
    
    if (not stateInQuote):
        copyPngFile (line) ## side effect
        memoRefs (line)  ## side effect
        convertedTags = convertObsidianTagsToMarkuaTags (line)
    else:
        convertedTags = line
        
    
    return convertedTags


##
# mainline
##

## 0. init
# pre cleanup
try:
    os.remove(stack)
except OSError as error:
    print (f'stack could not be removed ({error})')

try:
    os.remove(refs)
except OSError as error:
    print (f'refs could not be removed ({error})')

try:
    os.remove(missing)
except OSError as error:
    print (f'missing could not be removed ({error})')

shutil.rmtree ("manuscript")

mfiles = manuscript + '/*.md'
files = glob.glob(mfiles)
# for f in files:
#     os.remove(f)

rfiles = resources + '/*.png'
files = glob.glob(rfiles)
# for f in files:
#     os.remove(f)
    
stateInQuote = False

## 5. copy verbatim/* into manuscript/
shutil.copytree ("verbatim", "manuscript")

## 6. copy verbatimresources/* into manuscript/resources/
shutil.copytree ("verbatimresources", "manuscript/resources")


## 1.
with open(script) as file:
    fs = file.readlines()

    # for each file named in the script ...
    #  copy the file from the src to the manuscript directory
    #   change the new filenename to have no spaces
    #   insert a markua tag at the front of each file (for later referencing, conversion of Obsidian tags to markua tags)
    # side-effect: create a file 'refs' that contains every Obsidian reference to other files
    # side-effect: create file 'stack' that contains the name of every file mentioned in the script (maybe obsolete? intention: keep processing files until no more changes)
    # side-effect: while copying files to manuscript directory, change every Obsidian link to a markua link
    for f in fs:
        mdfile = mangleInputFilename (f) + '.md'
        inmdfile = input + '/' + mdfile
        outmdfile = reformatNameForLeanPub (manuscript +  '/' + mdfile)
        if (os.path.isfile (inmdfile)):
            tagAndCopyFile(inmdfile, outmdfile, makeTag  (f), filterObsidianLine)
            appendToStack (outmdfile)
        else:
            print (f'input file does not exist {inmdfile}')


## 2. create manuscript/book.md from script
##   rewrite filenames to new (markua) format (no spaces)
with open (script) as bookf:
    outfname = manuscript + '/' + 'book.md'
    with open (outfname, 'w') as outf:
        for line in bookf:
            print (reformatNameForLeanPub (line) + '.md', file=outf)
            
## 3. check for not-yet-written chunks (non-existent .md files)
##   scan file 'refs' (created in #1) and check that each file exists
##   if file does not exist, add its name to file 'missing'
with open (refs) as refs:
    with open (missing, 'a') as outf:
        for line in refs:
            name  =  line.strip ()
            if (os.path.isfile (name)):
                pass
            else:
                outf.write (name)
                outf.write ('\n')

## 4. print file 'missing' as a reminder of what hasn't been written yet
with open (missing) as missingf:
    for line in missingf:
        print (line, end="")
        
