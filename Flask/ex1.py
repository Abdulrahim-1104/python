from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def fun():
    return "Bismillah"

@app.route('/admin')
def admin():
    return 'This is admin page'

@app.route('/redirect')
def rederict():
    return redirect(url_for("fun")) 
def funnn():
    return 1

@app.route('/<name>') #passing argument for dir - one arg
def usename(name):
    return 'Hello '+name

@app.route('/<fname>/<lname>') #passing argument for dir - two arg
def username(fname,lname):
    return 'Hello '+fname+' '+lname

if "__main__" == __name__:
    app.run()