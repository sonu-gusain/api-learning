

# Product Inventory API 


from flask import Flask , jsonify , request

app = Flask(__name__)

data = []

@app.route("/get_data",methods= ["GET"])

def get():
    try:
      product_id = request.args.get("product_id")
  
      if  product_id:
        filter_data = []
        product_id = int(product_id)
        for i in data:
          if i["product_id"]==product_id:
            filter_data.append(i)
        return jsonify(filter_data)
      return jsonify(data)
    except Exception as e:
      return jsonify({"error server  down ":str(e)})
    

@app.route("/post_data",methods= ["POST"])

def post():
  try:
    product_data = request.get_json()

    if not product_data:
      return jsonify("provide your data")
    for i in product_data:
      if i not in data:
        data.append(i)
    return jsonify("data add sucessfully")
  except Exception as e:
    return jsonify({"error server  down ":str(e)})


@app.route("/update_data/<int:product_id>",methods= ["PUT"])

def put(product_id):
  try:
    product_data= request.get_json()

    if not product_data:
      return jsonify("error: provide your data")

    for i in data:
      if i["product_id"] == product_id:
        i.update(product_data)
        return jsonify("update successfully")
    return jsonify("product id not found")
  except Exception as e:
    return jsonify({"error server down ":str(e)})
  
@app.route("/delete_data",methods =["DELETE"])

def delete():
  try:
    product_data= request.get_json()

    for i in data:
      if i["product_id"] == product_data["product_id"]:
        data.remove(i)
        return jsonify("data remove succesfully ")
    return jsonify("mnot found data")
  except Exception as e:
    return jsonify({"error server down ":str(e)})

if __name__ == "__main__":
  app.run(debug = True)
