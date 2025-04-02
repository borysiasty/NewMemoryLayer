PLUGINNAME = $(shell basename $(PWD))
VERSION = $(shell sed -n 's/version=//p' metadata.txt)
ZIPFILE = $(HOME)/$(PLUGINNAME).$(VERSION).zip
.PHONY: help pylint pep8 zip

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  pep8        check Python code with pep8"
	@echo "  pylint      check Python code with pylint"
	@echo "  flake       check Python code with flake8"
	@echo "  zip         build zip package"


pep8:
	@pep8 --config=pep8 *.py


pylint:
	@pylint --disable=C0103,C0415,E0401,R0903,W0201 *.py


flake:
	@flake8 --ignore=D100,D101,D102,D103,D107,D400,D401,D403,F841,E203,E731,W503 --max-line-length=99 *.py 


zip:
	rm -f ${ZIPFILE}
	cd ..; zip -9r $(ZIPFILE) $(PLUGINNAME) -x "*.git/*" "*.gitignore" "*pyc" "*__pycache__/*" "*doc/*"
	@echo "Successfully zipped to" $(ZIPFILE)
