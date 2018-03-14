from form_test import app, config, helper
import flask
from flask import render_template, redirect, url_for, request
import random

from form_test.forms import TestForm


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = TestForm()
    for field in form:
        field.data = None
        form.process()

    return render_template('home.jinja2.html', form=form)