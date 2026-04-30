from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Masters(db.Model):
    __tablename__ = 'masters'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

class Mentor(db.Model):
    __tablename__ = 'mentor'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    master_id = db.Column(db.Integer, db.ForeignKey('masters.id', ondelete="CASCADE"))


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id', ondelete="CASCADE"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)  
