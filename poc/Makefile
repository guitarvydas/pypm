NODEMODULES=\
	node_modules/ohm-js \
	node_modules/yargs \
	node_modules/atob \
	node_modules/pako

# change this for your own environment
TOOLS=.

all: topls.py

full : $(NODEMODULES) tools topls.py

node_modules/ohm-js:
	npm install ohm-js
node_modules/yargs:
	npm install yargs
node_modules/atob:
	npm install atob
node_modules/pako:
	npm install pako

tools:
	(cd ./dr ; make)
	(cd ./prep ; make)
	(cd ./d2f ; make)
	(cd ./das2f ; make)
	(cd ./das2j ; make)
	echo '* ** *' done tools

ls.json : tools ls.drawio
	echo '* * *' generate.bash
	./generate.bash $(TOOLS) ls.drawio
	echo '* * * ' done generate.bash
	mv out.json ls.json

topls.py : ls.json transpile2py.bash pyemit.py
	echo '* * * ' transpile2py.bash
	./transpile2py.bash ls.drawio ls.json
	echo '* * * ' done transpile2py.bash
	mv top.py topls.py
	chmod a+x topls.py

clean:
	(cd ./dr ; make clean)
	(cd ./prep ; make clean)
	(cd ./d2f ; make clean)
	(cd ./das2f ; make clean)
	(cd ./das2j ; make clean)
	rm -f layer*
	rm -f preprocessed*
	rm -f duct?_*
	rm -f *.json
	rm -rf _*
	rm -f *~

npmstuff: node_modules/ohm-js node_modules/yargs node_modules/yargs-parser node_modules/atob node_modules/pako
	npm install ohm-js yargs atob pako

