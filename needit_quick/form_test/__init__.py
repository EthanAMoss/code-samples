from flask import Flask
from form_test import config

app = Flask(__name__)
app.config.from_object('form_test.config')
app.secret_key = 'HelloWorld'

from form_test import views

__version__ = 0.1
