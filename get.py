# get method of api in python .........

from flask import Flask

p = Flask(__name__)
@p.route("/hello_function",methods=["GET"])
def hello():
    return "hello sonu gusain"
if __name__=="__main__":
    p.run(debug=True)
    