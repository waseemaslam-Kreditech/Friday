# Address Parser

Python module to parse address string to house number, and street name.
- python version: >= 3

## Project Structure:
- **requirements.txt**: contains project requirements
- **addressline_parser.py**: contains AddressPraser class
- **test_addressline_parser.py**: cotains unittest cases
- **main.py**: start point, it reads samples.txt, parses it, then save the output to parsing_result.json file
- **samples.txt**: contains some addresses, i have added some more address format from the wiki page world wide - https://en.wikipedia.org/wiki/Address#Address_format
- **parsing_result.json**: contains AddressParser output
- **readme.md**

## How to run:

```
$ pip install -r requirements.txt
$ python main.py
```

## Unit testing:

```
$ python -m unittest test_addressline_parser.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

## Code coverage report:

```
$ coverage run -m unittest discover
$ coverage report
Name                         Stmts   Miss  Cover
------------------------------------------------
addressline_parser.py           10      0   100%
test_addressline_parser.py      21      0   100%
------------------------------------------------
TOTAL                           31      0   100%
```