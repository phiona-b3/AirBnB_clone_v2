#!/usr/bin/python3
from flask import Fask
"""starting a flask web application"""
app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    """return hello hbnb!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
