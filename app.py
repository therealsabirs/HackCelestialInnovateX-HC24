from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sabir@localhost:5433/SSIH'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from flask import session

@app.route('/set_session')
def set_session():
    session['data'] = 'Some value'
    return redirect(url_for('some_page'))

@app.route('/get_session')
def get_session():
    data = session.get('data', 'Default value')
    return render_template('some_page.html', data=data)





# Define Student, Alumni, and Faculty models
class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact_number = db.Column(db.String(20))
    password = db.Column(db.String(255), nullable=False)
    admission_year = db.Column(db.Integer)

     

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

   

class Faculty(db.Model):
    __tablename__ = 'faculty'
    faculty_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Jobs table
class Jobs(db.Model):
    __tablename__ = 'jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    number_of_positions = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    application_link = db.Column(db.String(255), nullable=False) 
# View Performance table
class ViewPerformance(db.Model):
    __tablename__ = 'viewperformance'
    performance_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    feedback = db.Column(db.Text)

    student = db.relationship('Student', backref='performances')

# Question table
# Question model
class Question(db.Model):
    __tablename__ = 'question'
    question_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    query_text = db.Column(db.Text, nullable=False)
    query_date = db.Column(db.DateTime, nullable=False)
    answer_text = db.Column(db.Text)
    alumni_id = db.Column(db.Integer, db.ForeignKey('alumni.alumni_id'))

    student = db.relationship('Student', backref='questions')
    alumni = db.relationship('Alumni', backref='questions_answered')

# Answers model
class Answers(db.Model):
    __tablename__ = 'answers'
    
    answer_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'), nullable=False)
    alumni_id = db.Column(db.Integer, db.ForeignKey('alumni.alumni_id'), nullable=False)
    answer_text = db.Column(db.Text, nullable=False)
    answer_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    question = db.relationship('Question', backref=db.backref('answers', lazy=True))
    alumni = db.relationship('Alumni', backref=db.backref('answers', lazy=True))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()  # Invalidate the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))
from functools import wraps
from flask import session, redirect, url_for, flash

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_type = session.get('user_type')
            if user_type != required_role:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('login'))  # Redirect to a safe page (e.g., index or login)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']
        
        user = None
        if user_type == 'student':
            user = Student.query.filter_by(email=email).first()
        elif user_type == 'alumni':
            user = Alumni.query.filter_by(email=email).first()
        elif user_type == 'faculty':
            user = Faculty.query.filter_by(email=email).first()
        
        if user and user.password == password:
            session['user_id'] = user.student_id if user_type == 'student' else user.alumni_id if user_type == 'alumni' else user.faculty_id
            session['user_type'] = user_type
            flash('Login successful', 'success')

            # Debug print to check session
            print(f"User ID: {session['user_id']}, User Type: {session['user_type']}")

            if user_type == 'student':
                return redirect(url_for('student_dashboard'))
            elif user_type == 'alumni':
                return redirect(url_for('alumni_dashboard'))
            elif user_type == 'faculty':
                return redirect(url_for('faculty_dashboard'))
        else:
            flash('Invalid login credentials', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')


# Define dashboards for student, alumni, and faculty (placeholder routes)
@app.route('/student_dashboard')
@role_required('student')
def student_dashboard():
        return render_template('student_dashboard.html')







@app.route('/alumni_details')
@role_required('student')
def alumni_details():
    alumni = Alumni.query.all()  # Fetch all alumni
    return render_template('alumni_details.html', alumni=alumni)


@app.route('/job_openings')
@role_required('student')
def job_openings():
    jobs = Jobs.query.all()  # Fetch all jobs
    return render_template('job_openings.html', jobs=jobs)


@app.route('/view_performance')
@role_required('student')
def view_performance():
    student_id = session.get('user_id')  # Get logged-in student's ID
    performance_records = ViewPerformance.query.filter_by(student_id=student_id).all()
    return render_template('view_performance.html', performance_records=performance_records)


@app.route('/ask_question', methods=['GET', 'POST'])
@role_required('student')
def ask_question():
    if request.method == 'POST':
        question_text = request.form['query_text']
        student_id = session.get('user_id')  # Assuming student_id is stored in session after login
        
        # Create a new question instance
        new_question = Question(
            student_id=student_id,
            query_text=question_text,
            query_date=datetime.utcnow()  # or use the current timestamp
        )
        
        # Add the new question to the database
        db.session.add(new_question)
        db.session.commit()
        
        flash('Question submitted successfully!', 'success')
        return redirect(url_for('student_dashboard'))
    
    return render_template('ask_question.html')




@app.route('/view_question')
@role_required('student')
def view_question():
    print("Session contents:", session)

    student_id = session.get('user_id')

    if not student_id:
        flash("You need to be logged in to view your questions.", 'danger')
        return redirect(url_for('login'))

    # Fetch questions for the student
    questions = Question.query.filter_by(student_id=student_id).all()

    # Fetch answers for each question
    question_answer_pairs = []
    for question in questions:
        answers = Answers.query.filter_by(question_id=question.question_id).all()
        question_answer_pairs.append((question, answers))

    return render_template('view_question.html', question_answer_pairs=question_answer_pairs)




@app.route('/debug_session')
def debug_session():
    return f"Session Content: {session}"


from flask import jsonify
from chatbot import Chatbot  # Assuming you have a chatbot class or logic

# Initialize your chatbot instance
chatbot = Chatbot()
chatbot_instance = Chatbot()  # Create an instance of the chatbot

@app.route('/chatbot', methods=['GET', 'POST'])
@role_required('student')
def chatbot():
    response = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')  # Get the user's input
        # Process the user input using the chatbot logic
        response = chatbot_instance.get_response(user_input)  # Assuming your chatbot instance has a get_response method

    return render_template('chatbot.html', response=response)













@app.route('/alumni_dashboard')
@role_required('alumni')
def alumni_dashboard():
    return render_template('alumni_dashboard.html')



@app.route('/answer_questions')
@role_required('alumni')
def answer_questions():
    questions = Question.query.filter(Question.answer_text.is_(None)).all()  # Fetch unanswered questions
    return render_template('answer_questions.html', questions=questions)


@app.route('/submit_answer/<int:question_id>', methods=['GET', 'POST'])
def submit_answer(question_id):
    # Fetch the specific question
    question = Question.query.get_or_404(question_id)
    
    if request.method == 'POST':
        # Get the submitted answer from the form
        answer_text = request.form['answer_text']
        alumni_id = session.get('alumni_id')  # Assuming alumni_id is stored in session after login
        
        # Create a new answer instance
        new_answer = Answers(question_id=question_id, alumni_id=alumni_id, answer_text=answer_text)
        
        # Add the new answer to the database
        db.session.add(new_answer)
        db.session.commit()
        
        flash('Answer submitted successfully!', 'success')
    
    # Fetch all answers for the current question
    answers = Answers.query.filter_by(question_id=question_id).all()
    
    # Render the template with the question and its answers
    return render_template('submit_answer.html', question=question, answers=answers)





@app.route('/add_job', methods=['GET', 'POST'])
@role_required('alumni')
def add_job():
    if request.method == 'POST':
        title = request.form['title']
        role = request.form['role']
        company = request.form['company']
        number_of_positions = request.form['number_of_positions']
        location = request.form['location']
        application_link = request.form['application_link']
        new_job = Jobs(title=title, role=role, company=company, number_of_positions=number_of_positions, location=location, application_link=application_link)
        db.session.add(new_job)
        db.session.commit()
        flash('Job added successfully!', 'success')
        return redirect(url_for('add_job'))

    return render_template('add_job.html')


@app.route('/edit_profile', methods=['GET', 'POST'])
@role_required('alumni')
def edit_profile():
    alumni_id = session.get('user_id')  # Get logged-in alumni's ID
    alumni = Alumni.query.get(alumni_id)

    if request.method == 'POST':
        alumni.name = request.form['name']
        alumni.email = request.form['email']
        alumni.contact_number = request.form['contact_number']
        alumni.company = request.form['company']
        alumni.role = request.form['role']
        alumni.linkedin_profile = request.form['linkedin_profile']
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('alumni_dashboard'))

    return render_template('edit_profile.html', alumni=alumni)





@app.route('/faculty_dashboard')
@role_required('faculty')
def faculty_dashboard():
    return render_template('faculty_dashboard.html')



@app.route('/add_student', methods=['GET', 'POST'])
@role_required('faculty')
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact_number = request.form['contact_number']
        password = request.form['password']
        admission_year = request.form['admission_year']
        new_student = Student(name=name, email=email, contact_number=contact_number, password=password, admission_year=admission_year)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('add_student'))

    return render_template('add_student.html')


@app.route('/edit_student', methods=['GET', 'POST'])
@role_required('faculty')
def edit_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student = Student.query.get(student_id)
        if student:
            student.name = request.form['name']
            student.email = request.form['email']
            student.contact_number = request.form['contact_number']
            db.session.commit()
            flash('Student information updated successfully!', 'success')
        else:
            flash('Student not found!', 'danger')
        return redirect(url_for('edit_student'))

    students = Student.query.all()  # Fetch all students for selection
    return render_template('edit_student.html', students=students)


@app.route('/view_students')
@role_required('faculty')
def view_students():
    students = Student.query.all()
    return render_template('view_students.html', students=students)


@app.route('/view_alumni')
@role_required('faculty')
def view_alumni():
    alumni = Alumni.query.all()
    return render_template('view_alumni.html', alumni=alumni)


@app.route('/add_alumni', methods=['GET', 'POST'])
@role_required('faculty')
def add_alumni():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact_number = request.form['contact_number']
        password = request.form['password']
        passout_year = request.form['passout_year']
        company = request.form['company']
        role = request.form['role']
        linkedin_profile = request.form['linkedin_profile']
        new_alumni = Alumni(name=name, email=email, contact_number=contact_number, password=password, passout_year=passout_year, company=company, role=role, linkedin_profile=linkedin_profile)
        db.session.add(new_alumni)
        db.session.commit()
        flash('Alumni added successfully!', 'success')
        return redirect(url_for('add_alumni'))

    return render_template('add_alumni.html')


@app.route('/view_questions')
@role_required('faculty')
def view_questions():
    questions = Question.query.all()
    return render_template('view_questions.html', questions=questions)

@app.route('/add_performance/<int:student_id>', methods=['GET', 'POST'])
@role_required('faculty')
def add_performance(student_id):
    if request.method == 'POST':
        semester = request.form['semester']
        subject = request.form['subject']
        grade = request.form['grade']
        feedback = request.form['feedback']
        
        # Create a new performance record
        new_performance = ViewPerformance(student_id=student_id, semester=semester, subject=subject, grade=grade, feedback=feedback)
        db.session.add(new_performance)
        db.session.commit()
        
        flash('Performance added successfully!', 'success')
        return redirect(url_for('view_students'))

    return render_template('add_performance.html', student_id=student_id)


@app.route('/view_all_questions')
@role_required('faculty')
def view_all_questions():
    # Fetch all questions, student names, and question IDs
    questions = db.session.query(
        Question.query_text, 
        Student.name.label('student_name'), 
        Question.question_id
    ).join(Student, Question.student_id == Student.student_id).all()

    # Prepare a list to hold questions and corresponding answers
    question_answer_pairs = []

    # For each question, fetch related answers and alumni names
    for query_text, student_name, question_id in questions:
        # Fetch answers along with alumni name for the current question
        answers_with_names = db.session.query(
            Answers.answer_text, 
            Alumni.name.label('alumni_name')
        ).join(Alumni, Answers.alumni_id == Alumni.alumni_id)\
         .filter(Answers.question_id == question_id).all()

        # Append question, student name, and answers/alumni info to the list
        question_answer_pairs.append({
            'query_text': query_text,
            'student_name': student_name,
            'answers': answers_with_names
        })

    # Pass the question and answer pairs to the template
    return render_template('view_all_questions.html', question_answer_pairs=question_answer_pairs)



@app.route('/add_job_faculty', methods=['GET', 'POST'])
@role_required('faculty')
def add_job_faculty():
    if request.method == 'POST':
        title = request.form['title']
        role = request.form['role']
        company = request.form['company']
        number_of_positions = request.form['number_of_positions']
        location = request.form['location']
        application_link = request.form['application_link']
        new_job = Jobs(title=title, role=role, company=company, number_of_positions=number_of_positions, location=location, application_link=application_link)
        db.session.add(new_job)
        db.session.commit()
        flash('Job added successfully!', 'success')
        return redirect(url_for('add_job_faculty'))

    return render_template('add_job_faculty.html')







from sqlalchemy import text

# Route to display the threads and comments for student
@app.route('/threads', methods=['GET', 'POST'])
def view_threads():
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    # Fetch threads and join with the appropriate user table based on user_type
    threads_query =text( '''
        SELECT t.thread_id, t.content, t.created_at, 
        CASE 
            WHEN t.user_type = 'student' THEN s.name 
            WHEN t.user_type = 'faculty' THEN f.name 
            WHEN t.user_type = 'alumni' THEN a.name 
        END AS username 
        FROM threads t
        LEFT JOIN student s ON t.user_id = s.student_id AND t.user_type = 'student'
        LEFT JOIN faculty f ON t.user_id = f.faculty_id AND t.user_type = 'faculty'
        LEFT JOIN alumni a ON t.user_id = a.alumni_id AND t.user_type = 'alumni'
        ORDER BY t.created_at DESC
    ''')
    threads = db.session.execute(threads_query).fetchall()

    # Fetch comments and join with the appropriate user table
    comments_query = text('''
        SELECT c.thread_id, c.comment_text, c.created_at, 
        CASE 
            WHEN c.user_type = 'student' THEN s.name 
            WHEN c.user_type = 'faculty' THEN f.name 
            WHEN c.user_type = 'alumni' THEN a.name 
        END AS username
        FROM comments c
        LEFT JOIN student s ON c.user_id = s.student_id AND c.user_type = 'student'
        LEFT JOIN faculty f ON c.user_id = f.faculty_id AND c.user_type = 'faculty'
        LEFT JOIN alumni a ON c.user_id = a.alumni_id AND c.user_type = 'alumni'
        ORDER BY c.created_at
    ''')
    comments = db.session.execute(comments_query).fetchall()

    return render_template('threads.html', threads=threads, comments=comments)

# Route to post a new thread
@app.route('/threads/new', methods=['POST'])
def post_thread():
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    content = request.form['content']
    user_id = session['user_id']
    user_type = session['user_type']

    # Insert new thread into the database
    # Insert into threads
    db.session.execute(
        text('INSERT INTO threads (user_id, user_type, content) VALUES (:user_id, :user_type, :content)'),
        {'user_id': user_id, 'user_type': user_type, 'content': content}
    )
    db.session.commit()

    flash('Your post has been added.', 'success')
    return redirect('/threads')

# Route to add a comment
@app.route('/threads/<int:thread_id>/comment', methods=['POST'])
def add_comment(thread_id):
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    comment_text = request.form['comment']
    user_id = session['user_id']
    user_type = session['user_type']

    # Insert new comment into the database
# Insert into comments
    db.session.execute(
        text('INSERT INTO comments (thread_id, user_id, user_type, comment_text) VALUES (:thread_id, :user_id, :user_type, :comment_text)'),
        {'thread_id': thread_id, 'user_id': user_id, 'user_type': user_type, 'comment_text': comment_text}
    )
    db.session.commit()

    flash('Your comment has been added.', 'success')
    return redirect('/threads')









# Route to display the threads and comments for qlumni
@app.route('/threads_alumni', methods=['GET', 'POST'])
def view_threads_alumni():
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    # Fetch threads and join with the appropriate user table based on user_type
    threads_query =text( '''
        SELECT t.thread_id, t.content, t.created_at, 
        CASE 
            WHEN t.user_type = 'student' THEN s.name 
            WHEN t.user_type = 'faculty' THEN f.name 
            WHEN t.user_type = 'alumni' THEN a.name 
        END AS username 
        FROM threads t
        LEFT JOIN student s ON t.user_id = s.student_id AND t.user_type = 'student'
        LEFT JOIN faculty f ON t.user_id = f.faculty_id AND t.user_type = 'faculty'
        LEFT JOIN alumni a ON t.user_id = a.alumni_id AND t.user_type = 'alumni'
        ORDER BY t.created_at DESC
    ''')
    threads = db.session.execute(threads_query).fetchall()

    # Fetch comments and join with the appropriate user table
    comments_query = text('''
        SELECT c.thread_id, c.comment_text, c.created_at, 
        CASE 
            WHEN c.user_type = 'student' THEN s.name 
            WHEN c.user_type = 'faculty' THEN f.name 
            WHEN c.user_type = 'alumni' THEN a.name 
        END AS username
        FROM comments c
        LEFT JOIN student s ON c.user_id = s.student_id AND c.user_type = 'student'
        LEFT JOIN faculty f ON c.user_id = f.faculty_id AND c.user_type = 'faculty'
        LEFT JOIN alumni a ON c.user_id = a.alumni_id AND c.user_type = 'alumni'
        ORDER BY c.created_at
    ''')
    comments = db.session.execute(comments_query).fetchall()

    return render_template('threads_alumni.html', threads=threads, comments=comments)

# Route to post a new thread
@app.route('/threads_alumni/new', methods=['POST'])
def post_thread_alumni():
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    content = request.form['content']
    user_id = session['user_id']
    user_type = session['user_type']

    # Insert new thread into the database
    # Insert into threads
    db.session.execute(
        text('INSERT INTO threads (user_id, user_type, content) VALUES (:user_id, :user_type, :content)'),
        {'user_id': user_id, 'user_type': user_type, 'content': content}
    )
    db.session.commit()

    flash('Your post has been added.', 'success')
    return redirect('/threads_alumni')

# Route to add a comment
@app.route('/threads_alumni/<int:thread_id>/comment', methods=['POST'])
def add_comment_alumni(thread_id):
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    comment_text = request.form['comment']
    user_id = session['user_id']
    user_type = session['user_type']

    # Insert new comment into the database
# Insert into comments
    db.session.execute(
        text('INSERT INTO comments (thread_id, user_id, user_type, comment_text) VALUES (:thread_id, :user_id, :user_type, :comment_text)'),
        {'thread_id': thread_id, 'user_id': user_id, 'user_type': user_type, 'comment_text': comment_text}
    )
    db.session.commit()

    flash('Your comment has been added.', 'success')
    return redirect('/threads_alumni')




# Route to display the threads and comments for faculty
@app.route('/threads_faculty', methods=['GET', 'POST'])
def view_threads_faculty():
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    # Fetch threads and join with the appropriate user table based on user_type
    threads_query =text( '''
        SELECT t.thread_id, t.content, t.created_at, 
        CASE 
            WHEN t.user_type = 'student' THEN s.name 
            WHEN t.user_type = 'faculty' THEN f.name 
            WHEN t.user_type = 'alumni' THEN a.name 
        END AS username 
        FROM threads t
        LEFT JOIN student s ON t.user_id = s.student_id AND t.user_type = 'student'
        LEFT JOIN faculty f ON t.user_id = f.faculty_id AND t.user_type = 'faculty'
        LEFT JOIN alumni a ON t.user_id = a.alumni_id AND t.user_type = 'alumni'
        ORDER BY t.created_at DESC
    ''')
    threads = db.session.execute(threads_query).fetchall()

    # Fetch comments and join with the appropriate user table
    comments_query = text('''
        SELECT c.thread_id, c.comment_text, c.created_at, 
        CASE 
            WHEN c.user_type = 'student' THEN s.name 
            WHEN c.user_type = 'faculty' THEN f.name 
            WHEN c.user_type = 'alumni' THEN a.name 
        END AS username
        FROM comments c
        LEFT JOIN student s ON c.user_id = s.student_id AND c.user_type = 'student'
        LEFT JOIN faculty f ON c.user_id = f.faculty_id AND c.user_type = 'faculty'
        LEFT JOIN alumni a ON c.user_id = a.alumni_id AND c.user_type = 'alumni'
        ORDER BY c.created_at
    ''')
    comments = db.session.execute(comments_query).fetchall()

    return render_template('threads.html', threads=threads, comments=comments)

# Route to post a new thread
@app.route('/threads_faculty/new', methods=['POST'])
def post_thread_faculty():
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    content = request.form['content']
    user_id = session['user_id']
    user_type = session['user_type']

    # Insert new thread into the database
    # Insert into threads
    db.session.execute(
        text('INSERT INTO threads (user_id, user_type, content) VALUES (:user_id, :user_type, :content)'),
        {'user_id': user_id, 'user_type': user_type, 'content': content}
    )
    db.session.commit()

    flash('Your post has been added.', 'success')
    return redirect('/threads_faculty')

# Route to add a comment
@app.route('/threads_faculty/<int:thread_id>/comment', methods=['POST'])
def add_comment_faculty(thread_id):
    if 'user_id' not in session or 'user_type' not in session:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    comment_text = request.form['comment']
    user_id = session['user_id']
    user_type = session['user_type']

    # Insert new comment into the database
# Insert into comments
    db.session.execute(
        text('INSERT INTO comments (thread_id, user_id, user_type, comment_text) VALUES (:thread_id, :user_id, :user_type, :comment_text)'),
        {'thread_id': thread_id, 'user_id': user_id, 'user_type': user_type, 'comment_text': comment_text}
    )
    db.session.commit()

    flash('Your comment has been added.', 'success')
    return redirect('/threads_faculty')





#Mentor Session
def get_current_alumni_id():
    # Assuming you store the alumni_id and user_type in session
    if 'user_id' in session and session.get('user_type') == 'alumni':
        return session['user_id']
    return None



class MentorSession(db.Model):
    __tablename__ = 'mentor_sessions'
    
    session_id = db.Column(db.Integer, primary_key=True)
    alumni_id = db.Column(db.Integer, db.ForeignKey('alumni.alumni_id'), nullable=False)  # Assuming alumni table exists
    session_title = db.Column(db.String(255), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    session_time = db.Column(db.Time, nullable=False)
    session_link = db.Column(db.Text, nullable=False)
    session_topic = db.Column(db.String(255))
    session_description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to Alumni, assuming Alumni model exists
    alumni = db.relationship('Alumni', backref=db.backref('mentor_sessions', lazy=True))

    def __repr__(self):
        return f'<MentorSession {self.session_title}>'

@app.route('/alumni_mentor_sessions', methods=['GET', 'POST'])
@role_required('alumni')
def create_mentor_session():
    if request.method == 'POST':
        session_title = request.form['session_title']
        session_date = request.form['session_date']
        session_time = request.form['session_time']
        session_link = request.form['session_link']
        session_topic = request.form['session_topic']
        session_description = request.form['session_description']
        alumni_id = get_current_alumni_id()  # Assuming you have a function to get the current alumni ID

        new_session = MentorSession(
            alumni_id=alumni_id,
            session_title=session_title,
            session_date=session_date,
            session_time=session_time,
            session_link=session_link,
            session_topic=session_topic,
            session_description=session_description
        )
        db.session.add(new_session)
        db.session.commit()
        flash('Mentor session created successfully!', 'success')
        return redirect(url_for('create_mentor_session'))

    sessions = MentorSession.query.filter_by(alumni_id=get_current_alumni_id()).all()
    return render_template('alumni_mentor_session.html', sessions=sessions)

@app.route('/alumni_mentor_sessions/<int:session_id>/edit', methods=['GET', 'POST'])
@role_required('alumni')
def edit_mentor_session(session_id):
    session = MentorSession.query.get_or_404(session_id)
    if session.alumni_id != get_current_alumni_id():
        abort(403)  # Prevent other alumni from editing
    if request.method == 'POST':
        session.session_title = request.form['session_title']
        session.session_date = request.form['session_date']
        session.session_time = request.form['session_time']
        session.session_link = request.form['session_link']
        session.session_topic = request.form['session_topic']
        session.session_description = request.form['session_description']
        db.session.commit()
        flash('Session updated successfully!', 'success')
        return redirect(url_for('create_mentor_session'))
    return render_template('edit_mentor_session.html', session=session)

@app.route('/alumni_mentor_sessions/<int:session_id>/delete', methods=['POST'])
@role_required('alumni')
def delete_mentor_session(session_id):
    session = MentorSession.query.get_or_404(session_id)
    if session.alumni_id != get_current_alumni_id():
        abort(403)  # Prevent other alumni from deleting
    db.session.delete(session)
    db.session.commit()
    flash('Session deleted successfully!', 'success')
    return redirect(url_for('create_mentor_session'))





@app.route('/mentor_sessions', methods=['GET'])

def view_mentor_sessions():
    current_date = datetime.utcnow().date()
    sessions = MentorSession.query.filter(MentorSession.session_date >= current_date).order_by(MentorSession.session_date).all()
    return render_template('mentor_sessions.html', sessions=sessions)




if __name__ == '__main__':
    app.run(debug=True)
