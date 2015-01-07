PROJECT=plonesocial.funkload

## see tests/Makefile for testing/benching

default: buildout

docker-build:
	docker.io build -t $(PROJECT) .

# re-uses ssh agent
# presupposes your buildout cache is in /var/tmp as configured in .buildout
# also loads your standard .bashrc
docker-run:
	docker.io run -i -t \
		--net=host \
		-v $(SSH_AUTH_SOCK):/tmp/auth.sock \
		-v $(HOME)/.gitconfig:/.gitconfig \
		-v $(HOME)/.gitignore:/.gitignore \
		-v /var/tmp:/var/tmp \
		-v $(HOME)/.bashrc:/.bashrc \
		-v $(HOME)/.buildout:/.buildout \
		-e SSH_AUTH_SOCK=/tmp/auth.sock \
		-v $(PWD):/app -w /app -u app $(PROJECT)

buildout: .virtualenv
	bin/buildout -v

devel: .virtualenv 
	bin/buildout -v -c devel.cfg

test:
	@cd tests && make test

clean:
	cd tests && make clean
	@echo "To nuke all scripts:  make cleanyesreally"

cleanyesreally:
	rm -rf .installed.cfg .virtualenv .zopeskel bin lib include *~ parts/*

.virtualenv:
	@rm -f bin/python
	@virtualenv --clear --no-site-packages --distribute .
	@bin/easy_install zc.buildout
	@touch $@

