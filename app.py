#app.py
from flask import Flask, url_for, render_template, request
import datetime
import code as c1
import code2 as c2  #alternative code

##https://stackoverflow.com/questions/62308385/how-should-i-be-importing-xml-for-display-in-flask#62314878
app = Flask(__name__)

@app.route('/')
def index():
    print("first test")
    return '''render_template(vars["template"],  vars=vars, dataset=dataset)'''

with app.test_request_context():
    x = datetime.datetime.now()

    #############################################
    # code to combine various license files
    #c1.code1()
    #############################################

    #alternative code:

    #This code reeds the license key and returns a list per trigram.
    #c2.code3()

    # This code reads a series of DSLS logfiles and returns structured usage data
    # Return is a csv files
    c2.code4()
