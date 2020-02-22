## Installation

### On Linux:

1) Do this once: `python3 -m venv venv`
2) Do this everytime before working on the app: `. venv/bin/activate`

Once you have your venv, install requirements:
```
pip install -r requirements.txt
```

### On Windows:
1) Install Python from their [website](https://www.python.org/downloads/windows/)
2) Install virtualenv: `pip install virtualenv`
3) Install virtualenvwrapper: `pip install virtualenvwrapper-win`
4) Make a virtual environment (this will also activate it): `mkvirtualenv AgileTrader`
5) Do this everytime before working on the app: `workon AgileTrader`

Once you have your virtualenv, install requirements:
```
pip install -r requirements.txt
```

## Running the App

from the root directory `agile_trader`:

### On Linux:

```
export FLASK_APP=app.py
python -m flask run
```

### On Windows:
```
set FLASK_APP=app.py
flask run
```

## Running the tests

also from the root directory `agile_trader`:

### On Linux and Windows
```
python -m unittest
```
or to run a specific test suite
```
python -m tests.test_TESTSUITENAME
```
