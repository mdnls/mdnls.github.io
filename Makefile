.PHONY : sty
sty :
	@sass styles:docs/styles

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
	@git commit public docs --quiet -m "Automated deploy commit" || echo "Deploying with no changes."
	@git push github main
