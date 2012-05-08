RIPE Funkload
=============

This installation is used for black-box (from the outside) http testing
of plonesocial.

Status: incomplete, work in progress.


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


RUNNING THE BENCH
=================

All of the below assumes you already have a plonesocial enabled site
running at localhost:9050/Plone

Switch plonesocial.microblog into the 'funkload' branch.

       gyst@sirius:plonesocial.microblog$ git checkout funkload

Start your plonesocial instance

      gyst@sirius:plonesocial.buildout$ bin/instance fg

You now have a @@microblog_funkload helper view.

      firefox http://localhost:9050/Plone/@@microblog_funkload

Run the bench

     gyst@sirius:plonesocial.funkload$ cd tests
     gyst@sirius:tests$ make

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

# 3) edit the new test suite

  # remove all external URL calls

# 4) test and re-edit until it works

../bin/fl-run-test test_AnonReadonly.py 

# 5) add the test suite to the Makefile test target

# 6) if applicable: add the new suite to the Makefile bench target

../bin/fl-run-bench -c1:2:5 ./test_AnonReadonly.py AnonReadonly.test_anon_readonly

# 7) clean up the development test output (in /tests/ !)

gyst@athena:~/plonesocial.funkload/tests$ make clean

# 8) add and commit new testsuite to git

git add .
git commit -a -m 'new test suite: anon_readonly'

Running tests and reports:
--------------------------

# cd tests
gyst@athena:~/plonesocial.funkload/tests$ make test
gyst@athena:~/plonesocial.funkload/tests$ make bench
gyst@athena:~/plonesocial.funkload/tests$ make report
