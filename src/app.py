from flask import Flask
from backends.InfiniteCampus import InfiniteCampus
from templates.boiler import plate
import random
app = Flask(__name__)



@app.get("/")
def main_page():
    inner = "<div class='MainWin'><h1>"+str(random.randint(-100,100))+"</h1></div>"
    return plate.replace("!INNER_HTML!", inner)