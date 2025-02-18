
# error handling with put post get delete method .... api in python (flask)



from flask import Flask , request , jsonify

p = Flask(__name__) 

data_user = []

@p.errorhandler(404)

def not_found(error):
      return jsonify({"error" : "not found"}) , 404


@p.errorhandler(500)

def server_error(error):
   return jsonify({"error" :  "somthing wanna wrong on server"}) , 500


@p.route("/get_user",methods=["GET"])

def get_method():
   try:
      name = request.args.get("name")

      filter_data = []

      if name:
        for i in data_user:
            if i["name"] == name:
                filter_data.append(i)
                
        if filter_data==[]:
            return jsonify("error : not found the user"),404
        else:
            return jsonify(filter_data)

      else:
           return jsonify(data_user)
        
   except Exception as e:
      return jsonify({" error : server down ": str(e)} ) , 500


@p.route("/get_email",methods=["GET"])

def get_email():
   try:
      user_email= request.args.get("email")
      for j in data_user:
        if j["email"] == user_email:
           return jsonify(j)
        else:
           return jsonify(f"error: not found the email {user_email}"),404
   except Exception as e:
       return jsonify({"error : server down ": str(e)} ) , 500

   
@p.route("/add_user",methods = ["POST"])

def add_user():
   try:
      data = request.get_json()
      if data ==[]:
        return jsonify("error data is blank")
   
      required_data = ["name","age","email"]
      for i in required_data:
        if i not in data:
         return jsonify(f"error data missing {i} ")
   
      for j in data_user:
        if j["email"] == data["email"]:
          return jsonify({"error: this email is already exsist ": data["email"]})
      data_user.append(data)

      return jsonify(f"add successfully data {data}")
   except Exception as e:
       return jsonify({"error : server down ": str(e)} ) , 500
   
   
@p.route("/update_user",methods=["PUT"])

def update_user():
   try:
      user_email = request.args.get("email")
      if not user_email:
         return jsonify({"error : email is blank put your email"}) , 400
      data = request.get_json()
      if not data:
         return jsonify({"error : your data is blank"}) , 400

      for i in data_user:
         if i["email"] == user_email:
            i.update(data)
            return jsonify({"message": "Data updated", "updated_data": i})
      return jsonify({"error":f" not found in useremail {user_email} "}),404
   except Exception as e:
      return jsonify({"error: server down ":str(e)}) , 500
   

@p.route("/delete_user",methods= ["DELETE"])

def delete_user():
   try:
      user_email = request.args.get("email")
      if not user_email:
         return jsonify({"error : email is blank put your email"}) , 400

      for i in data_user:
         if i["email"]==user_email:
            data_user.remove(i)
            return jsonify("data delete successfully")
         
      return jsonify({"error":f"this email  {user_email} is not in data "}) , 404
      
   except Exception as e:
     return jsonify({"error: server down ":str(e)}) , 500

if __name__ == "__main__":
   p.run(debug = True)
