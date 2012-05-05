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

bench: bench_microblog

bench_home:
	../bin/fl-run-bench ./test_Home.py Home.test_home || exit 0

bench_microblog:
	../bin/fl-run-bench ./test_Microblog.py Microblog.test_microblog || exit 0

# report

report: store report_microblog

report_home: 
	@../bin/fl-build-report --html -o reports results/home-bench.xml

report_microblog: 
	@../bin/fl-build-report --html -o reports results/microblog-bench.xml

soak: soak_microblog

soak_microblog:
	@while [ 1 ]; do ../bin/fl-run-bench -c150 --duration=3600 -m1 -M0 ./test_Microblog.py Microblog.test_microblog; rm *log *xml *bak; sleep 300; done

# utility targets

store: dirs
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
