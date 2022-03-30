from flask import Flask, render_template, request
from DAL import *

app = Flask(__name__)
# kfir was here

@app.route('/')
def index():
    return '<h1>Hello DevOps Class</h1>'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'


@app.route('/inventory')
def read_from_db():
    PATH = "C:\\Users\\user\\GreenPath\\SQL Practice\\"
    FILENAME = "Inventory.db"
    FILE = PATH + FILENAME
    con = set_sql_connection(FILE)  # Creates connection
    cur = set_cursor(con)  # Creates Cursor
    query = "SELECT * FROM Inventory"  # SQL QUERY
    data = cur.execute(query).fetchall()  # EXECUTING SQL QUERY
    dct = sort_as_dict(cur, data)
    close_sql_connection(con)  # Closing connection
    return f'{dct}'


@app.route('/insertitem', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        print("test")
        data = request.form['name']
        data2 = request.form['category']
        data3 = request.form['quantity']
        data4 = request.form['price']
        print(data, data2, data3, data4)
        #insert_new_record(data, data2, data3, data4)
        return render_template('insertitem.html', data=data)
    return render_template('insertitem.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
