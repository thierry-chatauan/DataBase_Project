from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, time, timedelta
from models import db, Jobs
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    jobs = Jobs.query.all()
    return render_template("home.html", jobs=jobs)

@app.route("/newRegister", methods=["GET", "POST"])
def newRegister():
    if request.method == "POST":
        costumer = request.form.get("costumer")
        drawing_number = request.form.get("drawing_number")
        machine = request.form.get("machine")
        operator = request.form.get("operator")

        now = datetime.now()
        start_date = now.date()
        start_time = now.time().replace(microsecond=0)

        new_job = Jobs(
            costumer=costumer,
            drawing_number=drawing_number,
            machine=machine,
            operator=operator,
            start_date=start_date,
            start_time=start_time
        )
        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("newRegister.html")

@app.route("/finish/<int:job_id>", methods=["POST"])
def finish_job(job_id):
    job = Jobs.query.get_or_404(job_id)
    job.finish()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    job = Jobs.query.get_or_404(job_id)

    if request.method == "POST":  # <-- only process form data on POST
        job.costumer = request.form.get("costumer")
        job.drawing_number = request.form.get("drawing_number")
        job.machine = request.form.get("machine")
        job.operator = request.form.get("operator")

        # Convert form values to proper types
        job.start_date = datetime.strptime(request.form.get("start_date"), "%Y-%m-%d").date()
        job.start_time = datetime.strptime(request.form.get("start_time"), "%H:%M").time()

        end_date = request.form.get("end_date")
        end_time = request.form.get("end_time")

        job.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        job.end_time = datetime.strptime(end_time, "%H:%M").time() if end_time else None

        # Recalculate total_time if both start and end exist
        if job.start_date and job.start_time and job.end_date and job.end_time:
            start_dt = datetime.combine(job.start_date, job.start_time)
            end_dt = datetime.combine(job.end_date, job.end_time)
            job.total_time = end_dt - start_dt

            print(f"Recalculated total_time: {job.total_time}")
        else:
            job.total_time = None


        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("edit_job.html", job=job)



@app.route("/delete/<int:job_id>", methods=["POST"])
def delete_job(job_id):
    job = Jobs.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/logout")
def logOut():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)