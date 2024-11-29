from chatbot import chatbot
from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from flask_recaptcha import ReCaptcha
import mysql.connector
import os
from waitress import serve  

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L",
    RECAPTCHA_SECRET_KEY="6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee"
))

recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'

# Database connectivity
conn = mysql.connector.connect(
    host='localhost', port='3306', user='root', password='sanchita15', database='register')
cur = conn.cursor()

@app.route("/index")
def home():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/forgot')
def forgot():
    return render_template('forgot.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
    users = cur.fetchall()
    if len(users) > 0:
        session['id'] = users[0][0]
        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials !!!')
        return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cur.execute("""INSERT INTO  users(name,email,password) VALUES('{}','{}','{}')""".format(name, email, password))
    conn.commit()
    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser = cur.fetchall()
    flash('You have successfully registered!')
    session['id'] = myuser[0][0]
    return redirect('/index')


@app.route('/suggestion', methods=['POST'])
def suggestion():
    email = request.form.get('uemail')
    suggesMess = request.form.get('message')

    cur.execute("""INSERT INTO  suggestion(email,message) VALUES('{}','{}')""".format(email, suggesMess))
    conn.commit()
    flash('Your suggestion is successfully sent!')
    return redirect('/index')


@app.route('/add_user', methods=['POST'])
def register():
    if recaptcha.verify():
        flash('New User Added Successfully')
        return redirect('/register')
    else:
        flash('Error Recaptcha') 
        return redirect('/register')


@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))



if __name__ == "__main__":
    print("App started successfully on http://127.0.0.1:5000/",)
    serve(app, host='0.0.0.0', port=5000)  
