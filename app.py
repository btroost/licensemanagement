#app.py
from flask import Flask, url_for, render_template, request
import datetime


app = Flask(__name__)

@app.route('/')
def index():
    print("first test")
    return '''render_template(vars["template"],  vars=vars, dataset=dataset)'''

with app.test_request_context():
    x = datetime.datetime.now()
    print(x)
