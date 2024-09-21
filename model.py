from app import db

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact_number = db.Column(db.String(20))
    password = db.Column(db.String(255), nullable=False)
    admission_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Student {self.name}>"

class Alumni(db.Model):
    __tablename__ = 'alumni'
    alumni_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact_number = db.Column(db.String(20))
    password = db.Column(db.String(255), nullable=False)
    passout_year = db.Column(db.Integer)
    company = db.Column(db.String(100))
    role = db.Column(db.String(100))
    linkedin_profile = db.Column(db.String(255))

    def __repr__(self):
        return f"<Alumni {self.name}>"

class Faculty(db.Model):
    __tablename__ = 'faculty'
    faculty_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Faculty {self.name}>"
