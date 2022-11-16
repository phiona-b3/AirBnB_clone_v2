#!/usr/bin/python3
"""another Flask function"""
app = Flask(__name__)
app.url_map.strict_slashes =  False

@app.route('/')
def hello_world():
  """returns a  Hello HBNB"""
  return "Hello HBNB!"

@app.route('/hbnb')
def hello_hbnb():
  """returns HBNB"""
  return "HBNB"

@app.route('/c/<text>')
def Text(text):
  """display C and the value of the text variable"""
  text = str(text).replace("_", " ")
  return 'C {}'.format(escape(text))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='5000', debug=True)
