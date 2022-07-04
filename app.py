from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Sign_in.html')

database={'Achref':'0000','Mustapha':'7777'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name=request.form['username']
    pwd=request.form['password']
    if name not in database:
        return render_template('Sign_in.html')
    else:
        if (database[name]!=pwd):
            return render_template('Sign_in.html')
        else:
            return render_template('user.html',user=name)
            