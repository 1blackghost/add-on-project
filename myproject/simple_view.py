'''
This .py file deals with simple view.
'''
#imports
from main import app
from flask import request,jsonify,session,abort
import json
from DBMS import helper


@app.route("/submit",methods=["POST","GET"])

def simple():
    hour=request.form["hour"]
    minute=request.form["minute"]
    am_pm=request.form["am_pm"]
    price=request.form["price"]
    price=price.split("₹")[1]
    uid=helper.insert_this(hour,minute,am_pm,"₹"+str(price))
    if "id" in session:
        session.pop("id")
    session["id"]=uid
    return json.dumps({'status':'ok'})

@app.route("/getData", methods=["POST", "GET"])
def userData():
    if "id" in session:
        data = helper.read_for(session["id"])
        data = { "status": data}

        json_string = json.dumps(data)

        return json_string
    else:
        abort(400, 'invalid')

@app.route("/getAll", methods=["POST", "GET"])
def userAll():

    data = tuple(helper.read_for())

    data_list = []
    for t in data:
        d = {"id": t[0], "hour": t[1], "minute": t[2], "am_pm": t[3], "price": t[4]}
        data_list.append(d)
    response = {"status": data_list}
    return jsonify(response)
