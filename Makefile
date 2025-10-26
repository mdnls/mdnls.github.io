.PHONY : sty
sty :
	@sass styles:public/styles

.PHONY : page
page : 
	@python build.py

.PHONY : all
all : sty page
	@cp -r tensorvis public/


.PHONY : watch
watch :
	@echo "Watching..."
	@fswatch . --exclude public | (while read; do make all; done)

.PHONY : deploy
deploy : all
	@git commit public --quiet -m "Automated deploy commit" || echo "Deploying with no changes."
