

# create api with jwt authontication


from fastapi import FastAPI , Depends , Header 
from typing import List
from pydantic import BaseModel
import jwt
import datetime


my_key = "mysecretkey"
gen = "HS256"

app = FastAPI()

product = []

class User(BaseModel):
    name : str
    password : int


class ProductDelete(BaseModel):
    product_id: int


class Products(BaseModel):
    product_id : int
    name : str
    category : str
    price : int


def genrate_token(username):
    gen_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=40)
    exp_time = {"name":username , "exp":gen_time.timestamp()}
    token = jwt.encode(exp_time, my_key , algorithm=gen)
    return token

def verify_token(authorization : str = Header(None)):
    verify = authorization.split()[1]
    token = jwt.decode(verify , my_key , algorithms=[gen])
    return token


@app.post("/login")

def login(key : User):
    if key.name == "sonu":
        if key.password == 8958:
            token = genrate_token(key.name)
            return token

@app.post("/post_data")

def post_data(prodt : List[Products] , token : str = Depends(verify_token)):
    try:
        for i in prodt:
            dublicate = False
            for j in product:
                if j["product_id"] == i.product_id:
                    dublicate = True
                    break

            if dublicate == False:
                product_data = {"product_id":i.product_id , "name":i.name , "category": i.category , "price":i.price}
                product.append(product_data)
        return ("data add successfully")
    except Exception as e:
        return {"error :  server down ": str(e)}
    

@app.get("/get_data")

def get_data(product_id : int=None , token : str = Depends(verify_token)):
    try:
        if product_id is None:
            return product
        
        filter_data = []
        for i in product:
            if i["product_id"] == product_id:
                filter_data.append(i)
        if filter_data:
            return filter_data
        else:
            return ("no data found")
    except Exception as e:
        return {"error :  server down ": str(e)}
    

@app.put("/put_data")

def put_data(prodt: List[Products] , token : str = Depends(verify_token)):
    try:
        for i in prodt:
            for j in product:
                if j["product_id"] == i.product_id:
                    j.update(i)
        return ("successfully data update")
    
    except Exception as e:
        return {"error : server down ": str(e)}


@app.delete("/delete_data")

def delete_data(prodt: List[ProductDelete] , token : str = Depends(verify_token)):
    try:
        for i in prodt:
            for j in product[:]:
                if j["product_id"] == i.product_id:
                    product.remove(j)
        return ("sucessfully delete data")

    except Exception as e:
        return {"error : server down ": str(e)}
    
