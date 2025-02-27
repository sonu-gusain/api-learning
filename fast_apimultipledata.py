# roll no. , name , subject in multiple update delete data

from fastapi import FastAPI ,Request
from pydantic import BaseModel
from typing import List

app = FastAPI()

data = []

class Users(BaseModel):
    roll_no : int
    name : str
    subject : str


@app.post("/post_method")

def post(u : List[Users]):
    try:
        for i in u:
            dublicate = False
            for j in data:
                if j["roll_no"] == i.roll_no:
                    dublicate = True
                    break
            if dublicate == False:
                user_data = {"roll_no":i.roll_no,"name":i.name,"subject":i.subject}
                data.append(user_data)
        return ("data add sucessfully")
    except Exception as e:
        return ({"error :  server down ":str(e)})

@app.get("/get_method")

def get(roll_no:int=None):
    try:
      if roll_no is None:
        return data
      
      filter_data=[]
      for i in data:
        if i["roll_no"] == roll_no:
          filter_data.append(i)
          return filter_data
      return ("no data found")
    except Exception as e:
        return ({"error :  server down ":str(e)})


@app.put("/update_method")

async def put(req:Request):
   try:
      user_data = await req.json()
      for i in user_data:
        
        for j in data:
           if i["roll_no"] == j["roll_no"]:
               j.update(i)

      return ("update sucessfully")
   
   except Exception as e:
    return ({"error : server down ":str(e)})         
           

@app.delete("/delete_method")

async def delete(req : Request):
   try:
      user_data = await req.json()

      for i in user_data:
         for j in data:
            if i["roll_no"] == j["roll_no"]:
               data.remove(j)
      return ("delete sucessfully ")
   except Exception as e:
    return ({"error : server down ":str(e)})  


