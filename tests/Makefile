## testing/benching

default: test

all: allclean test bench report

record:
	@./record

# test

test: test_noop test_microblog test_batch100 test_dummy test_dummy100

test_home:
	../bin/fl-run-test test_Home.py

test_noop:
	../bin/fl-run-test test_Noop.py

test_microblog:
	../bin/fl-run-test test_Microblog.py

test_batch100:
	../bin/fl-run-test test_Batch100.py

test_dummy:
	../bin/fl-run-test test_Dummy.py

test_dummy100:
	../bin/fl-run-test test_Dummy100.py

# bench

bench: bench_noop bench_microblog bench_batch100 bench_dummy bench_dummy100

bench_home:
	../bin/fl-run-bench ./test_Home.py Home.test_home || exit 0

bench_noop:
	../bin/fl-run-bench ./test_Noop.py Noop.test_noop || exit 0

bench_microblog:
	../bin/fl-run-bench ./test_Microblog.py Microblog.test_microblog || exit 0

bench_batch100:
	../bin/fl-run-bench ./test_Batch100.py Batch100.test_batch100 || exit 0

bench_dummy:
	../bin/fl-run-bench ./test_Dummy.py Dummy.test_dummy || exit 0

bench_dummy100:
	../bin/fl-run-bench ./test_Dummy100.py Dummy100.test_dummy100 || exit 0

# report

report: store report_noop report_microblog report_batch100 report_dummy report_dummy100

report_home: 
	@../bin/fl-build-report --html -o reports results/home-bench.xml

report_noop: 
	@../bin/fl-build-report --html -o reports results/noop-bench.xml

report_microblog: 
	@../bin/fl-build-report --html -o reports results/microblog-bench.xml

report_batch100: 
	@../bin/fl-build-report --html -o reports results/batch100-bench.xml

report_dummy: 
	@../bin/fl-build-report --html -o reports results/dummy-bench.xml

report_dummy100: 
	@../bin/fl-build-report --html -o reports results/dummy100-bench.xml

soak: soak_microblog

soak_microblog:
	@while [ 1 ]; do ../bin/fl-run-bench -c1 --duration=3600 -m1 -M0 ./test_Microblog.py Microblog.test_microblog; rm *log *xml *bak; sleep 300; done

# utility targets

store: dirs
	@mv *log results 2>/dev/null || exit 0
	@mv *xml results 2>/dev/null || exit 0

store2: dirs
	@mv *log results 2>/dev/null || exit 0
	@mv *xml results 2>/dev/null || exit 0

store3: dirs
	@mv *log results 2>/dev/null || exit 0
	@mv *xml results 2>/dev/null || exit 0

clean:
	@rm *pyc *~ *log *xml *.bak* 2>/dev/null || exit 0

allclean: clean dirs
	@rm -rf results/*
	@rm -rf reports/*

dirs:
	@[ -d results ] || mkdir results
	@[ -d reports ] || mkdir reports
