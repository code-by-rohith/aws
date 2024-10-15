from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works!"

@application.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8000, debug=True)