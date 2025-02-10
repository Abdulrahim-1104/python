from flask import Flask, request,render_template
app = Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("ex3.1.html")
    elif request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        return render_template("ex3.2.html",name=name,password=password)
# @app.route('/logged',methods=["GET")   # this is post method. defaultly the method in this place is get
# def logged():                                  # so while using get method use to access the data using request.args
#     name = request.form["username"]            # if the method id post use request.form in this code we use post method
#     password = request.form["password"]
#     return  render_template("ex3.2.html",name=name,password=password)
if __name__=="__main__":
    app.run()