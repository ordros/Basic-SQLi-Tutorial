from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3
import hashlib

app = Flask(__name__)

sql_content = ""

def check_password(hashed_password, user_password):
    return hashed_password == user_password
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM users WHERE username = \"" + username + "\" AND password = \"" + password + "\""
        print "[sql]:" + sql
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
            return redirect(url_for('secret_5ebe2294ecd0e0f08eab7690d2a6ee69'))
    return render_template('login.html', error=error)

@app.route('/secret_5ebe2294ecd0e0f08eab7690d2a6ee69')
def secret_5ebe2294ecd0e0f08eab7690d2a6ee69():
    return "Congratz! Flag is " + "BaSic_SQLi"
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
