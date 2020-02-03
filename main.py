from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'A simple demo of Continuous Integration of Flask web App on GCP.'


@app.route('/name/<value>')
def name(value):
    '''Dynamically generated website.'''
    val = {"value": value}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
