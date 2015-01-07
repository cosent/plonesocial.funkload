Plonesocial Funkload
====================

This installation is used for black-box (from the outside) http testing
of plonesocial.

WARNING
-------

| Do not install this package in your production site. This opens a security hole.
| This product is intended for testing development installations only!


Functionality provided:
-----------------------

- recording of tests
- executing functional tests
- executing load tests

Not every functional test can be parallelized safely into a load test.


INSTALLATION
============

See Makefile. 

System dependencies: gnuplot. 

Additional dependencies: tcpwatch.

Alternatively, use the provided docker.io::

    # compile the docker container
    make docker-build

    # enter the docker container
    make docker-run

    # run the buildout
    make


RUNNING THE BENCH
=================

The installation step above provides you with a Plone build.
Start Plone::

      bin/instance start

Create a Plone site.
Install the 'PloneSocial Microblog' add-on.

You now have a @@microblog_funkload helper view.

      firefox http://localhost:9050/Plone/@@microblog_funkload

Run the bench::

     gyst@sirius:plonesocial.funkload$ cd tests
     gyst@sirius:tests$ make all

Finally, point your browser at the ./tests/reports/ directory
to read the results of the various benches. YMMV.


DEVELOPMENT
===========

See separate Makefile in ./tests/

Recording of tests:
-------------------

# start plone

# record a testsuite 

gyst@athena:~/plonesocial.funkload$ cd tests/
gyst@athena:~/plonesocial.funkload/tests$ ./record anon_readonly

# configure your browser to use localhost:8091 as proxy
# disable all browser caching

# 1) do your browser session

# 2) ^C to break the test recorder

# 3) edit the new test suite::

  # remove all external URL calls

# 4) test and re-edit until it works::

  ../bin/fl-run-test test_AnonReadonly.py 

# 5) add the test suite to the Makefile test target

# 6) if applicable: add the new suite to the Makefile bench target::

  ../bin/fl-run-bench -c1:2:5 ./test_AnonReadonly.py AnonReadonly.test_anon_readonly

# 7) clean up the development test output (in /tests/ !)::

  gyst@athena:~/plonesocial.funkload/tests$ make clean

# 8) add and commit new testsuite to git::

  git add .
  git commit -a -m 'new test suite: anon_readonly'

