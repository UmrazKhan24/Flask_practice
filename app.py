from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Bijaiya World!</p>"



@app.route("/ping", methods=["GET"])
def ping():
    return "<p>Ping Bijaiya ping ping ping!</p>"

@app.route("/aboutus", methods=["GET"])
def aboutus():
    return "<p> We are the Bijaiya team. We are here to help you with your IT needs. </p>"


