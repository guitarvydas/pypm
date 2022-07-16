NODEMODULES=\
	node_modules/ohm-js \
	node_modules/yargs \
	node_modules/atob \
	node_modules/pako

# change this for your own environment
TOOLS=.

all: ls.py omitcomments.py omitcodequotes.py linkscraper.py

full : $(NODEMODULES) tools all

dev:
	touch dev.drawio
	make dev.py


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

dev.json : dev.drawio
	./generate.bash $(TOOLS) dev.drawio
	mv out.json dev.json

ls.json : ls.drawio
	./generate.bash $(TOOLS) ls.drawio
	mv out.json ls.json

omitcomments.json : omitcomments.drawio
	./generate.bash $(TOOLS) omitcomments.drawio
	mv out.json omitcomments.json

omitcodequotes.json : omitcodequotes.drawio
	./generate.bash $(TOOLS) omitcodequotes.drawio
	mv out.json omitcodequotes.json

linkscraper.json : linkscraper.drawio
	./generate.bash $(TOOLS) linkscraper.drawio
	mv out.json linkscraper.json

ls.py : ls.json
	./transpile2py.bash ls.drawio ls.json

dev.py : dev.json
	./transpile2py.bash dev.drawio dev.json

omitcomments.py : omitcomments.json
	./transpile2py.bash omitcomments.drawio omitcomments.json

omitcodequotes.py : omitcodequotes.json
	./transpile2py.bash omitcodequotes.drawio omitcodequotes.json

linkscraper.py : linkscraper.json
	./transpile2py.bash linkscraper.drawio linkscraper.json

# topls.py : ls.json transpile2py.bash pyemit.py
# 	echo '* * * ' transpile2py.bash
# 	./transpile2py.bash ls.drawio ls.json
# 	echo '* * * ' done transpile2py.bash
# 	mv top.py topls.py
# 	chmod a+x topls.py

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

