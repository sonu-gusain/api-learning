

# fast api school management system 

from fastapi import FastAPI , Request

app = FastAPI()

data = []

@app.get("/get_data")

def get(id : int = None):
    try:
        if id is None:
            return data
        for i in data:
            if i["id"] == id:
                return i
        return ("not found data")
    except Exception as e:
        return ({"error :  server down ": str(e)})

@app.post("/post_data")

async def post(req : Request):
  try:
    demo_data = await req.json()
    if not demo_data:
        return ("provide  your data")
    for i in demo_data:
        dublicate = False
        for j in data:
            if i["id"] == j["id"]:
                dublicate = True
                break
        if dublicate == False:
            data.append(i)
    return (f"data add sucessfully {i}")
  except Exception as e:
    return ({"error :  server down ": str(e)})

@app.put("/update_data/{id}")

async def put(id : int , req: Request):
  try:
    demo_data = await req.json()
    if not demo_data:
        return ("provide your data")
    
    for i in data:
        if i["id"] == id:
            i.update(demo_data)
    return (f"update sucessfully {demo_data}")
  
  except Exception as e:
    return ({"error : server down ": str(e)})
  

@app.delete("/delete_data")

async def delete(req : Request):
   try:
      demo_data = await req.json()
      if not demo_data:
        return ("provide your data")
      
      for i in data:
        if i["id"] == demo_data["id"]:
           data.remove(i)
      return ("delet sucessfully ")
   except Exception as e:
    return ({"error : server down ": str(e)})
  


