
# Student Database API multiple data 


from flask import Flask , request , jsonify

app = Flask(__name__)

student_data = []

@app.route("/get_data",methods = ["GET"])

def get():
  try:
    roll_no = request.args.get("roll_no")

    filter_data = []
    if roll_no:
      roll_no = int(roll_no)
      for i in student_data:
        if i["roll_no"] == roll_no:
          filter_data.append(i)
      
      if not filter_data:
        return jsonify("roll no. not found ")
      
      return jsonify(filter_data)
    
    return jsonify(student_data)    
  except Exception as e:
    return jsonify({"error : server down ":str(e)})


@app.route("/post_data",methods= ["POST"])

def post():
  try:
    data = request.get_json()
    filter_data = []
    
    for i in data:
      student_data.append(i)
      filter_data.append(i)
    return jsonify(f"sucessfull post data{filter_data}")
  except Exception as e:
    return jsonify({"error : server down ":str(e)})
  

@app.route("/update_data/<int:roll_no>",methods=["PUT"])

def roll(roll_no):
  try:
    data = request.get_json()
    if not data:
      return jsonify("data is blank")
    
    for i in student_data:
      if i["roll_no"] ==roll_no:
        i.update(data)
        return jsonify(f"data is succesfully update {data}")
    return jsonify("roll number not found")
  except Exception as e:
    return jsonify({"error : the server down" : str(e)})  


@app.route("/delete_data",methods= ["DELETE"])

def delete():
  try:
    data = request.get_json()

    if not data or "roll_no" not in data:
      return jsonify("error data not provide or roll number not provide")

    for i in student_data:
      if i["roll_no"] == data["roll_no"]:
        student_data.remove(i)
        return jsonify(f" delete succesfully {data}")
    return jsonify("error : roll number not found")
  except Exception as e:
    return jsonify({"error : the server down" : str(e)}) 


if __name__ == "__main__":
  app.run(debug=True)


