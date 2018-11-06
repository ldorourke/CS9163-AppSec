# Need to export as ENV var
export TEMPLATE_DIR = templates

DJANGO_DIR = appsec
PYTHONFILES = $(shell ls $(DJANGO_DIR)/*.py)

# build the static website describing the project:
website: $(INCS) $(HTML_FILES) 
	-git commit -a 
	git pull origin master
	git push origin master

# the rest of these targets may need to be tweaked for this project:
container:
	docker build -t scheduler docker


dblocal:
	python3 manage.py makemigrations
	python3 manage.py migrate
