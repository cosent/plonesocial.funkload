## testing/benching

default: test

all: allclean test bench report

record:
	@./record

# test

test: test_microblog

test_home:
	../bin/fl-run-test test_Home.py

test_microblog:
	../bin/fl-run-test test_Microblog.py

# bench

bench: bench_microblog_dummy

bench_home:
	../bin/fl-run-bench ./test_Home.py Home.test_home || exit 0

bench_microblog: bench_microblog_noop store2 bench_microblog_single store3 bench_microblog_batch10

bench_microblog_noop:
	../bin/fl-run-bench -l noop ./test_Microblog.py Microblog.test_noop || exit 0

bench_microblog_single:
	../bin/fl-run-bench -l single ./test_Microblog.py Microblog.test_microblog || exit 0

bench_microblog_batch10:
	../bin/fl-run-bench -l batch10 ./test_Microblog.py Microblog.test_batch10 || exit 0

bench_microblog_dummy:
	../bin/fl-run-bench -l batch10 ./test_Microblog.py Microblog.test_dummy || exit 0

# report

report: store report_microblog

report_home: 
	@../bin/fl-build-report --html -o reports results/home-bench.xml

report_microblog: 
	@../bin/fl-build-report --html -o reports results/microblog-bench.xml

soak: soak_microblog

soak_microblog:
	@while [ 1 ]; do ../bin/fl-run-bench -c10 --duration=3600 -m1 -M0 ./test_Microblog.py Microblog.test_microblog; rm *log *xml *bak; sleep 300; done

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
