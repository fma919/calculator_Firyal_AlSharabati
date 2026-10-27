# Optional Exercise 2 - Makefile wrapping PyBuilder
# Author: Firyal Al Sharabati
# NOTE: recipe lines must start with a TAB, not spaces.

.PHONY: clean install_deps test build all

clean:
	pyb clean

install_deps:
	pip install -r requirements.txt

test:
	pyb run_unit_tests

build:
	pyb publish

all: clean install_deps test build
