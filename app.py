import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome buddy fuc...er"

@app.route('/how are you')
def hell0():
    return 'I am good now'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

