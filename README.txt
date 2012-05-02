RIPE Funkload
=============

This installation is used for black-box (from the outside) http testing
of RIPE Plone services.

Functionality provided:
-----------------------

- recording of tests
- executing functional tests
- executing load tests

Not every functional test can be parallelized safely into a load test.


DEVELOPMENT
===========

# as root, for hardy

make predepends

# as normal user

hardy)gyst@athena:~/ripe.funkload$ make devel


Recording of tests:
-------------------

# start plone

(hardy)gyst@athena:~/ripe.labs$ bin/instance start

http://localhost:8090/manage

# add Plone site 'labstest' with the following extension profile:
      RIPE Labs: -tests- (integration tests: policy setup)
      RIPE Labs: -tests- (full local content)

http://localhost:8090/labstest/@@manage-portlets
# configure tag cloud: sizes=6 count=20 states=published
# keep refresh=3600


# record a testsuite 

(hardy)gyst@athena:~/ripe.funkload$ cd tests/
(hardy)gyst@athena:~/ripe.funkload/tests$ ./record anon_readonly

# configure your browser to use localhost:8091 as proxy
# disable all browser caching

# 1) do your browser session

# 2) ^C to break the test recorder

# 3) edit the new test suite

  # move the siteroot path to the configuration
  sed -i -e 's#/labstest##g' test_AnonReadonly.py
  sed -i -e 's#:8090#:8090/labstest#g' Anonreadonly.conf

  # remove all external URL calls (TweetMeme etc)!

# 4) test and re-edit until it works

../bin/fl-run-test test_AnonReadonly.py 

# 5) add the test suite to the Makefile test target

# 6) if applicable: add the new suite to the Makefile bench target

../bin/fl-run-bench -c1:2:5 ./test_AnonReadonly.py AnonReadonly.test_anon_readonly

# 7) clean up the development test output (in /tests/ !)

hardy)gyst@athena:~/ripe.funkload/tests$ make clean

# 8) add and commit new testsuite to git

git add .
git commit -a -m 'new test suite: anon_readonly'

Running tests and reports:
--------------------------

# cd tests
hardy)gyst@athena:~/ripe.funkload/tests$ make test
hardy)gyst@athena:~/ripe.funkload/tests$ make bench
hardy)gyst@athena:~/ripe.funkload/tests$ make report



PRODUCTION
==========


# as root, for hardy

make predepends ## TODO: centos

# as normal user

hardy)gyst@athena:~/ripe.funkload$ make prod

# edit tests/*conf to reflect server url

Running tests and reports:
--------------------------

# cd tests
hardy)gyst@athena:~/ripe.funkload/tests$ make test
hardy)gyst@athena:~/ripe.funkload/tests$ make bench
hardy)gyst@athena:~/ripe.funkload/tests$ make report

