from flask import Flask
from needit_quick import config

app = Flask(__name__)
app.config.from_object('needit_quick.config')
app.secret_key = 'HelloWorld'

from needit_quick import views

__version__ = 0.1