## startup targets

## see tests/Makefile for testing/benching

default: prod

predepends: .check_root
	@apt-get install python-setuptools Make
	@easy_install virtualenv
	#funkload
	@echo "for development: apt-get install python-dev gnuplot"

production: prod
prod: .virtualenv
	bin/buildout -v

devel: .virtualenv 
	bin/buildout -v -c devel.cfg


test:
	@echo "Run that from the ./tests directory, not from the buildout root."

clean:
	@echo "To remove test cruft: cd tests; make clean"
	@echo "To nuke all scripts:  make cleanyesreally"

cleanyesreally:
	rm -rf .installed.cfg .virtualenv .zopeskel bin lib include *~ parts/*

.virtualenv:
	@rm -f bin/python
	@virtualenv --clear --no-site-packages --distribute .
	@bin/easy_install zc.buildout
	@touch $@

update: 
	git pull

status: 
	@pwd && echo '==============================' && git $@ || echo '-------------------------'

push:
	@git $@

## utility targets

.check_root:
	@test "$$USER" = "root" || ( echo "Run that as root"; exit 1 )
