## Installation

### On Linux:

1) Do this once: `python3 -m venv venv`
2) Do this everytime before working on the app: `. venv/bin/activate`

Once you have your venv, install requirements:
```
pip install -r requirements.txt
```

To run the Flask app from the root directory (agile_trader):
```
export FLASK_APP=app.py
python -m flask run
```
