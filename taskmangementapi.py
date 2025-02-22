

# Task Management API


from flask import Flask , request as rq , jsonify as jn

a = Flask(__name__)

data = []
task_id_counter = 1

@a.route("/get_data",methods = ["GET"] )

def get_data():
    try:
        if data ==[]:
            return jn("no data in your task")
        return jn(data)
        
    except Exception as e:
        return jn({" errordata invalid ":str(e)}),500


@a.route("/post_data",methods = ["POST"])

def post_data():
    try:
      global task_id_counter
      taskdata = rq.get_json()
      if not taskdata or "title" not in taskdata:
        return jn("error :task title not required")

      task = {
        "task_id":task_id_counter,
        "title":taskdata["title"],
        "status":"pending"
      }
      
      data.append(task)
      task_id_counter += 1
      return jn(f"data add succesfully{task}")
    except Exception as e:
     return jn({" errordata invalid ":str(e)}),500


@a.route("/update_data",methods = ["PUT"])

def update_data():
   try:
    taskdata= rq.get_json()

    if not taskdata or "task_id" not in taskdata or "status" not in taskdata:
      return jn("error : task id or new status not required ")
    
    for i in data:
      if i["task_id"] == taskdata["task_id"]:
         i["status"] = taskdata["status"]
    return jn(f"data update succesfully: {i}")
    
    return jn("task not found"),404
   except Exception as e:
    return jn({"errordata invalid ":str(e)}),500


@a.route("/delete_data",methods = ["DELETE"])

def delete_data():
   try:
      taskdata = rq.get_json()
      if not taskdata or "task_id" not in taskdata:
        return jn("data invalid please put on ur data for delete")
      
      for i in data:
        if i["task_id"] == taskdata["task_id"]:
           data.remove(i)
           return jn("maessge : delete successfully")
      return jn("task not found")
   
   except Exception as e:
    return jn({"errordata invalid ":str(e)}),500

if __name__ == "__main__":
   a.run(debug=True)


