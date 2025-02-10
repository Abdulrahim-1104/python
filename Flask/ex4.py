from flask import Flask,render_template,request,redirect, url_for
app = Flask(__name__)
SPORTS = ['Cricket', 'Football', 'Batmitton', 'Chess', 'Carrom', 'Throwball']
REGISTRANTS = dict()
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template("ex4.2.html", sports=SPORTS)
    elif request.method == 'POST':
        temp_sport = request.form.get("sports")
        if temp_sport not in SPORTS:
            return render_template('ex4.4.html')
        else:
            name = request.form["name"]
            sports = request.form["sports"]
            REGISTRANTS[name] = sports
            return redirect(url_for('index'))
@app.route("/registrants")
def registrant():
    return render_template('ex4.3.html', registrants=REGISTRANTS)

if __name__ == '__main__':
    app.run()