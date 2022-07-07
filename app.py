from email import message
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('Sign_in.html')

# database={'Achref':'0000','Mustapha':'7777'}

# @app.route('/',methods=['POST','GET'])
# def login():
#     name=request.form['username']
#     pwd=request.form['password']
#     if name not in database:
#         return render_template('Sign_in.html')
#     else:
#         if (database[name]!=pwd):
#             return render_template('Sign_in.html')
#         else:
#             return render_template('user.html',user=name)

app.secret_key = 'VictoriaSecrets'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MySQL2022'
app.config['MYSQL_DB'] = 'music_user_data'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')   

@app.route('/Sign_in') 
def connect():
    return render_template('Sign_in.html')

@app.route('/Sign_up')
def sign_up():
    return render_template('Sign_up.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE user_name=%s AND pass=%s',(username,password))
            account = cursor.fetchone()
        except MySQLdb.Error:
            print('Error in establishing connection')
        
        if account :
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['user_name']
            return render_template('user.html',user=username)
        else:
            return render_template('Sign_in.html' , message='Invalid data!')

@app.route('/login/logout')
def logout():
    session.pop('loggedin' , None)
    session.pop('id' , None)
    session.pop('username' , None)
    return redirect(url_for('connect'))


@app.route('/register', methods=['GET', 'POST'])
def register():

    msg=''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE user_name=%s' ,[username])
        account = cursor.fetchone()

        if account :
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email adress!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username  or not password or not email:
            msg = 'Please fill out the form!'
        else:
            try:
                cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s)',[username, email, password])
                mysql.connection.commit()
            except MySQLdb.Error:
                print('Error in establishing connection')
            msg = 'You have successfully registred!'

    elif request.method == 'POST':
        msg='Please fill out the form!'
    return render_template('Sign_up.html', message=msg)