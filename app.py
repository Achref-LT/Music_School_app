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


@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE user_name=%s AND pass=%s',(username,password))
            account = cursor.fetchone()
        except MySQLdb.Error:
            print('error in establishing connection')
        
        if account :
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['user_name']
            return render_template('user.html',user=username)
        else:
            return'incorrect data'


