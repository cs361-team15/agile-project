from flask import Flask
from routes.views import routes

app = Flask(__name__)
app.register_blueprint(routes)
