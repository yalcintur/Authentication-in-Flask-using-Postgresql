'''
A login signup api
'''
#! /usr/bin/env python
import uuid
import hashlib
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Gumuldur123@localhost/test'
# for more information https://docs.sqlalchemy.org/en/13/core/engines.html

db = SQLAlchemy(app)

# defining the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    hsdpassword = db.Column(db.String(128), nullable=False)

    def _init_(self, email, username, password):
        self.email = email
        self.username = username
        self.hsdpassword = hsdpassword

# sh256 - password hashing + 
def encrypt_pass(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

# salting 
def salting_pass(sha_signature):
    salt = uuid.uuid4().hex
    salted_signature = sha_signature+':'+salt

    return salted_signature

# routing to signup - if appropriate , creating a new user in database
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    '''
    login func
    input: email, username, password
    output: error or not
    '''
    if request.method == 'GET':
        return 'You need to post for registering an user'
    elif request.method == 'POST':
        new_email = request.form['email']
        new_username = request.form['username']
        new_password = salting_pass(encrypt_pass(request.form['hsdpassword']))
        new_user = User(email=new_email, username=new_username, hsdpassword=new_password)
        db.session.add(new_user)
        db.session.commit()
        return 'Data is updated'
            

#login - comparing the credentials to the ones in database
@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    login func
    input: username, password
    output: successful or not
    '''
    if request.method == 'GET':

        return 'You need to post for logging in an user'
    elif request.method == 'POST':
        # taking in the given credentials
        crd_username = request.form['username']
        crd_password = encrypt_pass(request.form['hsdpassword'])

        try:
            #checking if user is present in the database
            if User.query.filter_by(username=crd_username).count():

                # finding the user in database where username in db is crd_username
                db_user = User.query.filter_by(username=crd_username).first()

                # removing the salt from password
                _hsdpassword, salt = db_user.hsdpassword.split(':')
                # comparing the crd_password to db_user's password
                if _hsdpassword == crd_password:
                    return 'Log in successful'
                else: 
                    return 'Wrong username or password'
            else:
                return f'No user named {crd_username} is present '

        except:
            return 'There has been an error!'

if __name__ == "__main__":
    app.run()
