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
#    print(x)

#    c1.code1()

#alternative code:
#    c2.code2()
    #code 2 leest een serie logfiles in en schrijft deze weg als csv files
    # met kolommen als computernaam en gebruikers key
    c2.code4()
    #C3 leest en serie logfiles en checkt het gebruik per gebruikersnaam
