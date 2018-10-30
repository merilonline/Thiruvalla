from flask import Flask
from flask_ask import Ask,question,statement,session
import random

app = Flask(__name__)
ask = Ask(app, '/')


@app.route("/hello")
def hello():
    return "Hello World!"

@ask.launch
def start_skill():
    welcome_message = 'Hello'
    return statement(welcome_message)

@ask.intent('GetNewFactIntent')
def intent():
    foo = ['Tiruvalla is located in Pathanamthitta district in the State of Kerala in South India.','The town is spread over an area of 27.94 square km','Tiruvalla is the biggest commercial centre in the district of Pathanamthitta','Tiruvalla lies on the banks of the rivers Manimala and Pamba','Tiruvalla is a land-locked region surrounded by irrigating streams and rivers','Tiruvalla is regarded as the "cultural capital of Central Travancore"','Tiruvalla is called "Land of non resident Indians']
    text = 'Hello, '+random.choice(foo)
    return statement(text)
