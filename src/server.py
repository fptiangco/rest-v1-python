from flask import Flask
app = Flask(__name__)

@app.route("/")
def v1():
    return "v1"

@app.route("/err")
def err():
    return "err"
