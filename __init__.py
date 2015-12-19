from flask import Flask, render_template, redirect, url_for, request

import xml.etree.ElementTree as ET
tree = ET.parse('static/user.xml')
root = tree.getroot()

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!" 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = False 
        for user in root.findall('user'):
            dbuser = user.find('name').text
            dbpass = user.find('pass').text
            if dbuser == username and dbpass==password:
                completion = True
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route('/secret')
def secret():
    return "You have successfully logged in"

if __name__ == '__main__':
    app.run(debug=True)
