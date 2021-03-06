.PHONY : sty
sty :
	@sass styles:public/styles

.PHONY : page
page : 
	@python build.py

.PHONY : all
all : sty page


.PHONY : watch
watch :
	@echo "Watching..."
	@fswatch . --exclude public | (while read; do make all; done)

.PHONY : deploy
deploy : all
	@git commit public --quiet -m "Automated deploy commit" || echo "Deploying with no changes."
	@git subtree push --prefix public github gh-pages
