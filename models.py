from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Jobs(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    costumer = db.Column(db.String(100), nullable=False)
    drawing_number = db.Column(db.String(100), nullable=False)
    machine = db.Column(db.String(100), nullable=False)
    operator = db.Column(db.String(100), nullable=False)

    start_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)

    end_date = db.Column(db.Date, nullable=True)
    end_time = db.Column(db.Time, nullable=True)

    total_time = db.Column(db.Interval, nullable=True)

    def finish(self):
        """Mark job as finished now and calculate duration"""
        now = datetime.now()
        self.end_date = now.date()
        self.end_time = now.time().replace(microsecond=0)

        start_dt = datetime.combine(self.start_date, self.start_time)
        end_dt = datetime.combine(self.end_date, self.end_time)
        self.total_time = end_dt - start_dt

        print(self)

    def total_hours(self):
        if self.total_time:
            return round(self.total_time.total_seconds() / 3600, 2)
        return None
    
    @property
    def total_hours_minutes(self):
        if self.total_time:
            total_minutes = int(self.total_time.total_seconds() // 60)
            hours, minutes = divmod(total_minutes, 60)
            return f"{hours:02d}:{minutes:02d}"
        return None

    def __repr__(self):
        return (f"<Job {self.id} {self.machine} {self.costumer} "
                f"{self.drawing_number} {self.start_date} {self.start_time} "
                f"{self.end_date} {self.end_time} {self.total_time}>")
                
    
    