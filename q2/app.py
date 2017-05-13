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
        print "[sql]: " + sql
        cur.execute(sql)
        rows = cur.fetchall()
        content = ""
        for row in rows:
            content += str(row)
        print content
        sql_content = content
        global sql_content
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
    content = "<b>Flag is not here. <br>Another table contain flag.</b><br>"
    content += "Your query result is"
    content += "<br>"
    content += sql_content
    return content

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, threaded=True, debug=False)
