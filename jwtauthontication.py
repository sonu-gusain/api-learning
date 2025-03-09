
# jwt authontication in api 


import jwt 
import datetime

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_jwt_token(username):
    expire_token = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
    verify = {"sub":username,"exp":expire_token}
    token = jwt.encode(verify, SECRET_KEY, algorithm= ALGORITHM)
    return token

def verify_jwt_token(token_no):
    token = jwt.decode(token_no , SECRET_KEY , algorithms=[ALGORITHM])
    return token

if __name__ == "__main__":
    user = "naveen"
    token_create = create_jwt_token(user)
    print(f"genrate token:   {token_create}")
    
    result = verify_jwt_token(token_create)
    print(f"the verification:  {result}")


# second example in jwt 


import jwt 
import datetime

key = "mysecertkey"
new = "HS256"

def genrate_token(user):
    expiry = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes= 50)
    token = {"name":user , "exp":expiry}
    genrate = jwt.encode(token , key , algorithm= new)
    return genrate

def genrate_verify_token(tokens):
    verify = jwt.decode(tokens , key , algorithms= [new])
    return verify

if __name__ == "__main__":
    users = "name"
    create = genrate_token(users)
    print(f"token create:   {create}")

    print(genrate_verify_token(create))

    