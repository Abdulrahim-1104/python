from flask import Flask, render_template, jsonify
import mysql.connector
app = Flask(__name__)
connecter = mysql.connector.connect(host='localhost',user='root',password='1104',database='rahim_library')
mycursor = connecter.cursor()
@app.route('/')
def index():
    try:
        mycursor.execute('SELECT * FROM users')
        data = mycursor.fetchall()
        mycursor.close()
        return render_template('ex5.html', data=data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
