from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('form.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('contact added successfully')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return "edit contact"

@app.route('/delete')
def delete():
    return "delete contact"

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
