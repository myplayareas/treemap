from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/v1")
def treemap_v1():
    return render_template('index.html')

@app.route("/v2")
def treemap_v2():
    return render_template('index2.html')

@app.route("/about")
def about():
    return 'Apache Cassandra Treemap'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404