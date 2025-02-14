
# flask api methods of put post delete get:.


from flask import Flask, request, jsonify

data_user = []

p = Flask(__name__)

@p.route("/add_user", methods = ["POST"])
def add_user(): 
  data = request.get_json()
  name = data.get("name")
  age = data.get("age")
  data_user.append({"name":name,"age":age})
  return jsonify(f"massage add {name} and {age} successfully add")

@p.route("/update_user",methods = ["PUT"])
def update_user():
  data = request.get_json()
  name = data.get("name")
  new_age = data.get("age")
  for i in data_user:
    if i["name"]==name:
      i["age"]=new_age
      return jsonify(f"massage :the {name} is succesfully change")
  return jsonify("massage"f"not found  user : {name} ")  

@p.route("/delete_user",methods=["DELETE"])
def delete_user():
  data = request.get_json()
  name = data.get("name")
  
  for j in data_user:
    if j["name"]==name:
      data_user.remove(j)
      return jsonify(f"massagethe user name : {name} is succesfully delete")
  return jsonify(f"massage the user name : {name} is not found")

@p.route("/get_data",methods=["GET"])
def get_data():
  return jsonify(data_user)

if __name__=="__main__":
  p.run(debug=True)
