
# two or more data in flask post push put delete method 

from flask import Flask , request , jsonify

user_data= []

a = Flask(__name__)

@a.route("/add_data",methods = ["POST"])
def add_data():
    data = request.get_json()
    users = data.get("users",[])
    for i in users:
        name = i.get("name")
        age = i.get("age")
        user_data.append({"name":name,"age":age})
    return jsonify(f"message : the add succesfully {name}")


@a.route("/get_data",methods= ["GET"])
def get_data():
    return jsonify(user_data)


@a.route("/update_data",methods= ["PUT"])
def update_data():
    data = request.get_json()
    name = data.get("name")
    new_age= data.get("age")

    for j in user_data:
        if j["name"]==name:
            j["age"] = new_age
            return jsonify(f"message: the name is {name} and update age successfully")
    return jsonify("user not found")


@a.route("/delete_data",methods = ["DELETE"])
def delete_data():
    data = request.get_json()
    name = data.get("name")

    for k in user_data:
        if k["name"]==name:
            user_data.remove(k)
            return jsonify(f"message : the name {name} remove succesfully")
    return jsonify(f"message : the name is {name} not found")

if __name__=="__main__":
    a.run(debug=True)

