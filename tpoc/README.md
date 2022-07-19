Textual Proof of Concept

- of 0D components written in Python 

- to build a simple script that copies files from an Obsidian directory into a leanpub directory

- converting Obsidian .png links to leanpub resources/ links
- converting Obsidian links to leanpub links

usage:
> python3 top.py

design:
see  pmcopy.drawio


legend:
- blue boxes are python 0D Leaves
- gray boxes are python 0D Containers, i.e. compositions of components and message routing between them
- green circles, with 100% opacity and solid outlines, are input ports
- yellow circles, with 100% opacity and solid outlines,  are output ports
- green circles, with 50% opacity and dotted outlines, are input ports that are implicitly connected to green circles with shadows with exactly the same name
- green circles, with 50% opacity and dotted outlines and shadows, are input ports that are implicitly connected to green circles with/out shadows with exactly the same name, if implicit ports appear on the edges of a gray box, their values are delegated to the inside of the boxes
- gray circles are init-time constants that output their (atomic) values once at the beginning of a run
- purple boxes are like blue boxes, but, I use purple to remind me that these Leaves contain multiple states (this is not necessary in machine-generated code, but may be useful during hand-compilation of the POC (I'm no longer sure if this distinction is necessary, even for hand-compiled code))

- gray boxes with no ports contain initialized instance variables

- gradient shading is meaningless and is used only as syntactic sugar to aid in reading the diagram

atoms:
strings - valid Python strings

connections:
arrows - uni-directional message flows (there are no bi-directional message flows)
implicit - implicit connections go from 
	- green circles with shadows to green circles 50% dotted
	- green circles with shadows to green circles with shadows (downward delegation)

syntax:
- syntax has been chosen to be entered simply using a QWERTY keyboard, in the future we may bind Unicode characters to certain keystrokes
.name - control flow constructs in this uber-language

notes:
there is probably the need for output port delegation (upward from yellow 50% dotted to yellow with shadow), but, this POC doesn't use them, YAGNI


WARTS in POC (Proof of Concept):
- Omit__Code__Quotes should be a character-by-character state machine, but is implemented as a set of mutually recursive functions (that form a larger state machine)
