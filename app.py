from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Jobs
from datetime import datetime, time, timedelta
from sqlalchemy import text

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
    return render_template('home.html', jobs=jobs, title="Home")

@app.route('/newRegister', methods=['GET', 'POST'])
def newRegister():
    if request.method == 'POST':
        try:
            # Get form data
            costumer = request.form['costumer']
            drawing_number = request.form['drawing_number']
            machine = request.form['machine']
            operator = request.form['operator']
            date_start = request.form['date-start']
            time_start = request.form['time-start']
            date_end = request.form['date-end']
            time_end = request.form['time-end']

            print(costumer, drawing_number, machine, operator, date_start, time_start, date_end, time_end)

            # Convert date and time strings into Python objects
            print("Convert date and time strings into Python objects")
            start_datetime = datetime.strptime(f"{date_start} {time_start}", "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(f"{date_end} {time_end}", "%Y-%m-%d %H:%M")
            
            print(start_datetime, end_datetime)
            # Calculate total time
            total_time = end_datetime - start_datetime
            total_hours = total_time.total_seconds() / 3600  # Convert to hours

            hours = int(hours_float)
            minutes = int((hours_float - hours) * 60)
            seconds = int(round((((hours_float - hours) * 60) - minutes) * 60))

            # Convert to proper time format using timedelta
            total_time_formatted = str(total_time)  # This automatically formats as "HH:MM:SS"

            print(f"Total time: {total_time}, Total hours: {total_hours}, Formatted time: {total_time_formatted}")
            # Extract date and time components
            start_date = start_datetime.date()
            start_time = start_datetime.time()
            end_date = end_datetime.date()
            end_time = end_datetime.time()

            # Create new Job entry
            new_job = Jobs(
                name=operator,
                machine=machine,
                costumer=costumer,
                drawing_number=drawing_number,
                start_date=start_date,
                start_time=start_time,
                end_date=end_date,
                end_time=end_time,
                total_time=total_hours  # Store total time in hours
            )
            print("New job created:", new_job)

            # Save into database
            db.session.begin()
            db.session.add(new_job)
            db.session.commit()
            db.session.flush()

            print("Job committed to database")
            flash(f'Job registered successfully! Total time: {total_hours:.2f} hours', 'success')
            return redirect(url_for('home'))
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('newRegister.html', title="New Register")

    return render_template('newRegister.html', title="New Register")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)