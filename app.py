from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Jobs

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

@app.route('/')
def login():
    return render_template('login.html', title="Login")

@app.route('/home')
def home():
    jobs = Jobs.query.all()
    return render_template('home.html',jobs=jobs, title="Home")


@app.route('/newRegister')
def newRegister():
    return render_template('newRegister.html',  title="New Register")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)