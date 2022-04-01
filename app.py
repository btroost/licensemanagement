#app.py
from flask import Flask, url_for, render_template, request
import datetime
import code as c1


##https://stackoverflow.com/questions/62308385/how-should-i-be-importing-xml-for-display-in-flask#62314878
app = Flask(__name__)

@app.route('/')
def index():
    print("first test")
    return '''render_template(vars["template"],  vars=vars, dataset=dataset)'''

with app.test_request_context():
    x = datetime.datetime.now()
    print(x)

    c1.code1()
