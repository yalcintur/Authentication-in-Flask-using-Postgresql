from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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