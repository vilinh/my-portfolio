import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)
dataf = open("app/static/data.json",  encoding="utf-8")
data = json.load(dataf)

class Polaroid:
    def __init__(self, caption, pic):
        self.caption = caption
        self.pic = pic


pols = [
    Polaroid("drawing", "./static/img/drawing.png"),
    Polaroid("cooking", "./static/img/cooking.png"),
    Polaroid("traveling",
             "./static/img/traveling.png")
]


@app.route('/')
def index():

    projs = data['projs']
    exps2 = data['experiences']
    hobbies = data['polaroids']

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), projects=projs, polaroids=hobbies, experiences=exps2)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"), polaroids=pols)
