#!/usr/bin/python3
from flask import Flask
"""init the flask"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """return a string"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", post="5000", debug=True)
