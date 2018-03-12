import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello World"
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    hobbies = request.form['hobbies']
    age = request.form['age']
    address = request.form['address']
    data = [name, hobbies, age, address]
    conn = sqlite3.connect('user.db')
    db = conn.cursor()
    query = 'insert into users_data values("' + name + '", ' + age + ', "' + hobbies + '", "' + address + '")'
    db.execute(query)
    conn.commit()
    conn.close()
    return ("saved! <br>" + ", ".join(data))


app.run(debug=True)
