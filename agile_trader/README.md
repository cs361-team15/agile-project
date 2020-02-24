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

from the back-end's root directory `agile_trader`:

### On Linux:

```
export FLASK_APP=app.py
python -m flask run
```

### On Windows:
```
set FLASK_APP=app.py
python -m flask run
```

## Running the tests

also from the back-end's root directory `agile_trader`:

### On Linux and Windows
```
python -m unittest
```
or to run a specific test suite
```
python -m tests.test_TESTSUITENAME
```

## Pushing changes to Heroku

### On Linux

### On Windows

1) Make sure you have the [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) installed
2) Login to Heroku through the command line: `heroku login`
3) From the back-end's root folder (\agile_trader), convert your local directory into a git module: `git init`
4) Connect it to the Heroku repo: `git remote add heroku https://git.heroku.com/agile-trader.git`
*note: if successful, you should be able to type `git remote -v` and see that URL listed for fetching and pushing*

Now whenver you make a change that you want to push to the Heroku repo, you can just use the following commands:
```
git add .
git commit -m "commit message"
git push heroku master
```
That last command will also automatically rebuild the app.

To spin up the app use 
```
heroku ps:scale web=1
```
If successful you should be able to visit agile-trader.herokuapp.com to make sure its working. To check the logs use `heroku logs` or login to Heroku.com and use the dashboard.

Because we are on the free tier, we have a certain number of hours per month our Heroku dynos can be running. For now, when you are done working on the app it'd probably be best to scale it down to conserve hours.
```
heroku ps:scale web=0
```


