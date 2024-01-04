from flask import Flask

view = Flask(__name__)

@view.route("/")
def represent():
  return "<h1> The Heading </h1><br><br><p> Body or the content </p>"

@view.route("/home")
def repo():
  return "<h1> The Home </h1><br><br><p> Body of the home </p>"

@view.route("/view")
def rev():
  return "<h1> The View </h1><br><br><p> Body of the View </p>"
  
if __name__ == '__main__':
  # app.run(host='0.0.0.0', port=8080)
  print("Hello!")