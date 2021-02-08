from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Super fancy database
PROFILE = {
        "success": True,
        "data": {
            "last_updated": "2/3/2021, 8:48:51 PM",
            "username": "JChumlee",
            "role": "Telecoms Student",
            "color": "#FF7F50"
           
        }
    }

TANK = []
tank_id = 0

@app.route("/")
def home():
    return "ECSE3038 - Lab 2 - 620104371"

#Returns all of the data in the database
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def get_profile():
    if request.method == "GET":
        return jsonify(PROFILE)

    elif request.method == "POST":
        #current date and time
        #now = datetime.now()
        dt = datetime.now().strftime("%c")

        PROFILE["data"]["last_updated"] = dt
        PROFILE["data"]["username"] = (request.json["username"])
        PROFILE["data"]["role"] = (request.json["role"])
        PROFILE["data"]["color"] = (request.json["color"])

        return jsonify(PROFILE)

    elif request.method == "PATCH":
        #current date and time
        dt = datetime.now().strftime("%c")
    
        data = PROFILE["data"]

        r = request.json
        r["last_updated"] = dt
        attributes = r.keys()
        for attribute in attributes:
            data[attribute] = r[attribute]

        return jsonify(PROFILE)    


###############################################################

#Returns all of the data in TANK
@app.route("/data", methods=["GET", "POST"])
def tank_data():
    if request.method == "GET":
        return jsonify(TANK)  

    elif request.method == "POST":
        global tank_id

        tank_id += 1

        r = request.json
        r["id"] = tank_id
        TANK.append(r)
        return jsonify(TANK)
   
 
@app.route('/data/<int:id>', methods=["PATCH", "DELETE"])
def tank_id_methods(id):
    if request.method == "PATCH":
        for i in TANK:
            if i["id"] == id:
                r = request.json
                attributes = r.keys()

                for attribute in attributes:
                    i[attribute] = r[attribute]

        return jsonify(TANK)
    
    elif request.method == "DELETE":
        for i in TANK:
            if i["id"] == id:
                TANK.remove(i)

        return jsonify(TANK)

if __name__ == "__main__":
    app.run(
        debug=True,
        #port = 3000,
        #host = "0.0.0.0"
    )