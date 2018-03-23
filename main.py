import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    # return "Hello World"
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    if not name:
        return (render_template('index.html', err="enter name"))
        
    hobbies = request.form['hobbies']
    
    age = request.form['age']
    print (type(age))
    if not age.isdigit():
        return render_template('index.html', err="enter valid age")

    age = int(age)
    print(age < 1 or age > 100)
    if age < 1 or age > 100:
        print('here')
        return render_template('index.html', err="Age should be between 1 to 100")

    print('saving')
    address = request.form['address']
    print (name)
    data = [name, hobbies, str(age), address]
    conn = sqlite3.connect('user.db')
    db = conn.cursor()
    query = 'insert into users_data values("' + name + '", ' + str(age) + ', "' + hobbies + '", "' + address + '")'
    db.execute(query)
    conn.commit()
    conn.close()
    return ("saved! <br>" + ", ".join(data))

@app.route('/search', methods = ['GET', 'POST'])
def search():

    if request.method == 'GET': 
        return render_template('./search.html')

    name = request.form['name']
    print (name)
    conn = sqlite3.connect('user.db')
    db = conn.cursor()
    query = 'select * from users_data where name="' + name + '";'
    print (query)
    data = db.execute(query)
    results = data.fetchall()
    print ("fetch all...", len(results))
    foo = {}
    print ('results...', results)
    
    for res in results:
        print ('res...', res)
        foo['name'] = res[0]
        foo['age'] = res[1]
        foo['hobbies'] = res[2]
        foo['address'] = res[3]
        
        print ('foo...', res)
    return (render_template('./search.html', foo=foo))
    

app.run(debug=True)
