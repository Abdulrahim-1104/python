from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('ex2.html') # it take the path correctly because flask automatically check named templates
@app.route('/admin')                   # if the name is not template it wont work if you named differently you have to
def admin():                           # mention it in the Flask(__name__,template_folder="foldername")
    return  render_template('ex2.html',content="admin")
if __name__=="__main__":
    app.run()