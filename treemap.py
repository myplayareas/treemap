from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return 'Apache Cassandra Treemap'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404