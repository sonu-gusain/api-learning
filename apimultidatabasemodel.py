
# multiple data update delete add get in fastapi through basemodel


from fastapi import FastAPI 
from pydantic import BaseModel
from typing import List

app = FastAPI()

data = []

class User(BaseModel):
    id : int
    name : str
    age : int


class delete_data(BaseModel):
    id :int


@app.post("/post_data")

def post(user_data: List[User]):
    try:
        for i in user_data:
            dublicate = False
            for j in data:
                if j["id"] == i.id:
                    dublicate = True
                    break
            if dublicate == False:
                user_data_add = {"id" : i.id , "name": i.name , "age" : i.age}
                data.append(user_data_add)

        return (" add sucessfully data")
    except Exception as e:
        return ({"error  : server down ": str(e)})

@app.get("/get_data")

def get(id : int=None ):
    try:
        if id is None:
            return data
        
        filter_data = []
        for i in data:
           if i["id"] == id:
               filter_data.append(i)
               return filter_data
        
        return ("no found data")
    except Exception as e:
        return ({"error :  server down ": str(e)})
    

@app.put("/update_data")

def put(updated : List[User]):
    try:
        for i in updated:
            for j in data:
                if j["id"] == i.id:
                    j.update(i)

        return ("sucessfully updated")
    
    except Exception as e:
        return ({"error : server down ": str(e)})   


@app.delete("/delete_data")

def deleted(deleted : list[delete_data]):
    try:
        for i in deleted:
            for j in data:
                if j["id"] == i.id:
                    data.remove(j)

        return ("sucessfully delete ")
    
    except Exception as e:
        return ({"error : server down ": str(e)})  
        
