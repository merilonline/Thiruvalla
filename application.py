from flask import Flask
from flask_ask import Ask,question,statement,session
import random

app = Flask(__name__)
ask = Ask(app, '/')



@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/fact")
def rand():
    foo = ['its beautiful', 'its hot', 'its good', 'its calm', 'its peaceful']
    return random.choice(foo)

@ask.intent('GetNewFactIntent')
def intent():
    foo = ['its beautiful', 'its hot', 'its good', 'its calm', 'its peaceful']
    text = 'Hello There, '+random.choice(foo)
    return statement(text)
