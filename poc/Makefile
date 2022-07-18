NODEMODULES=\
	node_modules/ohm-js \
	node_modules/yargs \
	node_modules/atob \
	node_modules/pako

# change this for your own environment
TOOLS=.

all: pm.py

full : $(NODEMODULES) tools all

leaf-dev:
	touch dev.drawio
	make dev.py

old-dev:
	echo this bootstrap version does not support container.in -> container.out
	touch dev.drawio
	#make dev.py


dev:
	touch pm.drawio
	make pm.py

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

mdfilereader.json : mdfilereader.drawio
	./generate.bash $(TOOLS) mdfilereader.drawio
	mv out.json mdfilereader.json

# Containers
perfilelinkscraper.json : perfilelinkscraper.drawio
	./generate.bash $(TOOLS) perfilelinkscraper.drawio
	mv out.json perfilelinkscraper.json

pm.json : pm.drawio
	./generate.bash $(TOOLS) pm.drawio
	mv out.json pm.json



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

mdfilereader.py : mdfilereader.json
	./transpile2py.bash mdfilereader.drawio mdfilereader.json

# Containers
perfilelinkscraper.py : perfilelinkscraper.json
	./transpile2py.bash perfilelinkscraper.drawio perfilelinkscraper.json

pm.py : pm.json
	./transpile2py.bash pm.drawio pm.json


# topls.py : ls.json transpile2py.bash pyemit.py
# 	echo '* * * ' transpile2py.bash
# 	./transpile2py.bash ls.drawio ls.json
# 	echo '* * * ' done transpile2py.bash
# 	mv top.py topls.py
# 	chmod a+x topls.py

dontuse-clean:
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

