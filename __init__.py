from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3
import hashlib

app = Flask(__name__)

def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM users WHERE username = \"" + username + "\" AND password = \"" + password + "\""
        print "[sql]: " + sql
        cur.execute(sql)
        rows = cur.fetchall()
        if rows != []:
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route('/secret')
def secret():
    content = "<b>Flag is not here. <br>flag is admin password.</b><br>"
    return content

if __name__ == '__main__':
    app.run(debug=False)
