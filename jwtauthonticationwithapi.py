
# jwt authorization with api 



from fastapi import FastAPI , Depends , Header 
from pydantic import BaseModel
import jwt 
from typing import List
import datetime

key = "mysecretkey"
gen = "HS256"


app = FastAPI()

student = []

class User(BaseModel):
    name : str
    password : int

class Students(BaseModel):
    roll_no : int
    name : str 
    age : int 


def create_token(username):
    token = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes= 40)
    new = {"name" : username , "exp" : token.timestamp()}
    cr_token = jwt.encode(new , key , algorithm= gen)
    return cr_token 

def verify_token(authorization: str = Header(None)):
    token = authorization.split()[1]
    verify = jwt.decode(token , key , algorithms= [gen])
    return verify
    

@app.post("/login")

def login(create : User):
    if create.name == "sonu" and create.password == 12345:
        token = create_token(create.name)
        return token
    

@app.post("/post_data")

def post(data : List[Students] , token :str = Depends(verify_token)):
    try:
        for i in data:
            dublicate = False
            for j in student:
                if j["roll_no"] == i.roll_no:
                    dublicate = True
                    break
            if dublicate == False:
                user_data = {"roll_no":i.roll_no , "name":i.name , "age":i.age}
                student.append(user_data)
        return ("data add sucessfully")
    except Exception as e:
        return {"error :  server down ": str(e)}
    

@app.get("/get_data")

def get(roll_no : int = None , token : str = Depends(verify_token)):
    try:
        if roll_no is None:
            return student
        filter_data = []
        for i in student:
            if i["roll_no"] == roll_no:
                filter_data.append(i)
        if filter_data:
            return filter_data
        else:
            return ("no data found")
 
    except Exception as e:
        return {"error :  server down ": str(e)}
    

@app.put("/put_data")
                
def put(data : List[Students] , token : str = Depends(verify_token)):
    try:
        for i in data:
            for j in student:
                if j["roll_no"] == i.roll_no:
                    j.update(i)
        return ("update successfully")
    
    except Exception as e:
        return {"error : server down ": str(e)}
    

@app.delete("/delete_data")

def delete(data : List[Students] , token : str = Depends(verify_token)):
    try:
        for i in data:
            for j in student:
                if j["roll_no"] == i.roll_no:
                    student.remove(j)
        return ("sucessfully deleted ")
    
    except Exception as e:
        return {"error : server down ": str(e)}
    
