.PHONY : sty
sty :
	@sass styles:public/styles

.PHONY : page
page : 
	@python build.py

.PHONY : all
all : sty page
	@cp -R public/


.PHONY : watch
watch :
	@echo "Watching..."
	@fswatch . --exclude public | (while read; do make all; done)

.PHONY : deploy
deploy : all
	@cp -R public/* docs
	@git commit public docs --quiet -m "Automated deploy commit" || echo "Deploying with no changes."
	@git push github main
