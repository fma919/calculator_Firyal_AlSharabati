# calculator_Firyal_AlSharabati

Lab 6 – Automatic Build using PyBuilder (Software Tools Lab, Fall 2026-2027)
**Student:** Firyal Al Sharabati

A simple calculator built and tested automatically with PyBuilder.

## Functions
`add`, `subtract`, `multiply`, `divide`, plus the graded exercise functions
`modulus`, `power`, and `square_root`.

## Project structure
```
calculator_Firyal_AlSharabati/
├── build.py
├── requirements.txt
├── src/main/python/calculator_Firyal_AlSharabati/__init__.py
└── tests/unittest/calculator_Firyal_AlSharabati/test_calculator_Firyal_AlSharabati.py
```

## How to build
```
pip install pybuilder
pyb run_unit_tests     # run the unit tests
pyb                    # full build (default task: publish)
```

Run the tests without PyBuilder:
```
python -m unittest tests.unittest.calculator_Firyal_AlSharabati.test_calculator_Firyal_AlSharabati
```

## Optional: Makefile
`make test`, `make build`, `make clean`, `make all` wrap the PyBuilder commands.
