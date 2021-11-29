from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


app.run(debug=True, load_dotenv=True)
