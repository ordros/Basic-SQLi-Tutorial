# Flask-Login-App-Tutorial
Tutorial for how to make a simple Flask login app, with a XML database
***
Hello, today I am going to teach you how to setup a Flask login page. 

First, you want to install virtual environment on your system. This can be done in the command line using pip install virtualenv.
Navigate the folder where you want flask to reside in, and in there enter the command pip install flask.
Next, you want to verify setup was correct, so let's create a Hello World app.

***
Create a file anywhere, I named mine __init__.py
In that anywhere, create two folders, static and templates.

__init__.py should contain the following code: 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World"

if __name__== "__main__":
    app.run()
```

Next, you want to go to where you installed Flask, open the script directory in command prompt, and enter activate
From there, navigate to your __init__.py location, and then run it using python __init__.py 
In your browser, navigate to http://127.0.0.1:5000/ to verify that it worked.
The words Hello World should appear on your screen.
I found this video to be useful in the setup:

[![Flask Setup](https://i.ytimg.com/vi_webp/98JY6MvumVs/mqdefault.webp)](http://www.youtube.com/watch?v=98JY6MvumVs)
***
Now to create the login page. In order to do so, let's go back into __init__.py.
We need to add a route for login, so below your index function, add the following code: 
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)
 ```

Let's make a template called login.html
It's contents will be: 
```html
<html>
  <head>
    <title>Flask Intro - login page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <h1>Please login</h1>
      <br>
      <form action="" method="post">
        <input type="text" placeholder="Username" name="username" value="{{
          request.form.username }}">
         <input type="password" placeholder="Password" name="password" value="{{
          request.form.password }}">
        <input class="btn btn-default" type="submit" value="Login">
      </form>
      {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}
      {% endif %}
    </div>
  </body>
</html>
```
Visit http://127.0.0.1:5000/login to verify that this works.
We also need to have a location that this page goes to, so let's add a secret route too!
```python  
@app.route('/secret')
def secret():
    return "This is a secret page!"
```
  You also need to update your imports, they are now: 
```python
  from flask import Flask, render_template, redirect, url_for, request
```
***
Now that you have seen a basic login system, let's setup a database. We will be using a simple XML database.
Create a file called user.xml
In that file add the following: 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user>
  <name>ihoegen</name>
  <pass>Hunter12</pass>
</user>
<user>
  <name>leet1337</name>
  <pass>python</pass>
</user>
```
You can use your own passwords, or add as many as you would like. Put this file in the same directory as __init__.py.

Now we need to update our file to process XML.
At the top, add an import for the python XML library

```python
import xml.etree.ElementTree as etree
```
Also, you're going to have to rework your login method. It will now look like: 
```python
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
```
It uses a for loop to process the XML and compare the username and passwords.
***
Your file structure will look like
```

--Main Folder
    --__init__.py
    --Static
        --user.xml
    --Templates
        --login.html
```
        
Thanks for reading!
