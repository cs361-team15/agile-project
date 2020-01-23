USE VENV

On Linux

1) Do this once: python3 -m venv venv
2) Do this everytime before working on the API: . venv/bin/activate

Once you have your venv, install flask: pip install Flask

To run our dev server do 
  export FLASK_APP=api.py
  python -m flask run
