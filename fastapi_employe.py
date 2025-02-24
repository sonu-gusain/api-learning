

# employee managment system

from fastapi import FastAPI , Request

app = FastAPI()
data = []

@app.get("/get_data")
def get_data(emp_id: int=None):
    try:
        if emp_id is None:
            return data
        
        filter_data = []
        for i in data:
            if i["emp_id"] == emp_id:
                filter_data.append(i)
                return filter_data
        return ("error : no data found")
        
    except Exception as e:
      return ({"error: surver  down":str(e)})


@app.post("/post_data")
async def post(req:Request):
  try:
    emp_data = await req.json()

    if not emp_data:
        return ("error : please data provede")
    
    for i in emp_data:
        dublicate = False
        for j in data:
            if j["emp_id"] == i["emp_id"]:
                dublicate = True
                break
        if dublicate ==False:
            data.append(i)

    return ("data sucessfully add ")
  except Exception as e:
    return ({"error: surver  down":str(e)})

@app.put("/update_data/{emp_id}")

async def update_data(emp_id : int, req :Request):
   try:
      emp_data = await req.json()
      for i in data:
        if i["emp_id"]==emp_id:
           i.update(emp_data)
        
      return (f"sucessfully update data{emp_data}")
   except Exception as e:
    return ({"error: surver down":str(e)})


@app.delete("/delete_data")

async def delete_data(req :Request):
   try:
      emp_data = await req.json()
      if not emp_data:
         return ("provide your data")
      for i in data:
         if i["emp_id"] == emp_data["emp_id"]:
            data.remove(i)
      return ("data remove successfully")
   except Exception as e:
    return ({"error: surver down":str(e)})

