from flask import Flask
from backends.InfiniteCampus import InfiniteCampus

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"