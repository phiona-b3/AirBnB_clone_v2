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

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='5000', debug=True)
