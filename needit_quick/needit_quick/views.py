from needit_quick import app, config, helper
import flask
from flask import render_template, redirect, url_for, request
import random

from needit_quick.forms import SearchForm


@app.route('/', methods=['GET', 'POST'])
def home_page():
    search_form = SearchForm()

    if search_form.validate_on_submit():
        return redirect(url_for("search_results", item=search_form.search_text.data, radius=search_form.search_radius.data))

    return render_template('home.jinja2.html', search_form=search_form, categories=helper.categories)


@app.route('/search')
def search_results():
    item = request.args.get('item', None)
    radius = request.args.get('radius', None)

    search_form = SearchForm()
    search_form.search_text.default = item
    search_form.search_radius.default = float(radius)
    search_form.process()

    random.seed(len(item))

    results = helper.search_results[random.randint(0, len(helper.search_results) - 1)]

    return render_template('search.jinja2.html', search_form=search_form, results=results, radius=radius, item=item)


@app.route('/map', methods=['GET', 'POST'])
def map_page():
    if request.method == 'POST':
        search_form = SearchForm()

        brand = request.form.get('brand')
        prices = request.form.getlist('prices[]')
        item = request.form.get('item')
        radius = request.form.get('radius')

        search_form.search_text.default = item
        search_form.search_radius.default = float(radius)
        search_form.process()

        return render_template('maps.jinja2.html', search_form=search_form, brand=brand, prices=prices,
                               stores=helper.stores)

    else:
        return redirect(url_for("home_page"))


@app.route('/category')
def category_page():
    category = request.args.get('category', None)

    items = helper.categories.get(category, None)

    if not items:
        return redirect(url_for('home_page'))

    search_form = SearchForm()

    return render_template('category.jinja2.html', search_form=search_form, category=category, items=items)
