from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/fact")
def rand():
    foo = ['its beautiful', 'its hot', 'its good', 'its calm', 'its peaceful']
    return random.choice(foo)