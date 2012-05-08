## testing/benching

default: test

all: allclean test bench report

record:
	@./record

# test

test: test_noop test_microblog test_batch100 test_batch1000 

test_home:
	../bin/fl-run-test test_Home.py

test_noop:
	../bin/fl-run-test test_Noop.py

test_microblog:
	../bin/fl-run-test test_Microblog.py

test_batch100:
	../bin/fl-run-test test_Batch100.py

test_batch1000:
	../bin/fl-run-test test_Batch1000.py

test_dummy:
	../bin/fl-run-test test_Dummy.py

test_dummy100:
	../bin/fl-run-test test_Dummy100.py

# bench

bench: bench_noop bench_microblog bench_batch100 bench_batch1000

bench_home:
	../bin/fl-run-bench ./test_Home.py Home.test_home || true

bench_noop:
	../bin/fl-run-bench ./test_Noop.py Noop.test_noop || true

bench_microblog:
	../bin/fl-run-bench ./test_Microblog.py Microblog.test_microblog || true

bench_batch100:
	../bin/fl-run-bench ./test_Batch100.py Batch100.test_batch100 || true

bench_batch1000:
	../bin/fl-run-bench ./test_Batch1000.py Batch1000.test_batch1000 || true

bench_dummy:
	../bin/fl-run-bench ./test_Dummy.py Dummy.test_dummy || true

bench_dummy100:
	../bin/fl-run-bench ./test_Dummy100.py Dummy100.test_dummy100 || true

# report

report: store report_noop report_microblog report_batch100 report_batch1000

report_home: 
	@../bin/fl-build-report --html -o reports results/home-bench.xml

report_noop: 
	@../bin/fl-build-report --html -o reports results/noop-bench.xml

report_microblog: 
	@../bin/fl-build-report --html -o reports results/microblog-bench.xml

report_batch100: 
	@../bin/fl-build-report --html -o reports results/batch100-bench.xml

report_batch1000: 
	@../bin/fl-build-report --html -o reports results/batch1000-bench.xml

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
