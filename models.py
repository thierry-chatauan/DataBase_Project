from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jobs(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    machine = db.Column(db.String(50), nullable=False)
    costumer = db.Column(db.String(50), nullable=False)
    drawing_number = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    total_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f"<Jobs{self.name} {self.machine} {self.costumer} {self.drawing_number} {self.start_date} {self.start_time} {self.end_date} {self.end_time} {self.total_time}>" 