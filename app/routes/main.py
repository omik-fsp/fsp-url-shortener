from flask import request, render_template, redirect, url_for, jsonify
from app import app
from app.utils.main import helloWorld, addUrlDB, getUrlDB
# Sooner than later will be better to use import *


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/api/shorturl/new', methods=['POST'])
def newUrl():
    response = addUrlDB(request.form['url'])

    return jsonify(response)


@app.route('/api/shorturl/<string:shorten_url>')
def rediUrl(shorten_url):
    response = {}

    response['url'] = getUrlDB(shorten_url)

    if response['url']:
        return redirect(response['url'], code=302)
    else:
        del response['url']
        response['error'] = 'Short ID not found in database'

        return jsonify(response)


@app.route('/hello-world')
def hello():
    response = helloWorld()

    return jsonify({'response': response})
