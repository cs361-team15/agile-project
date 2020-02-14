# project/app.py
from flask import Flask
from .services.application_service import ApplicationService

app = Flask(__name__)

appService = ApplicationService()

@app.route('/')
def foobar():
    return appService.handler_test()

@app.route('/test')
def handler_test():
    return "This is a new test"