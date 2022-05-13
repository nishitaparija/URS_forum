from flask import Flask, render_template, request,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/urs'
db = SQLAlchemy(app)

class Rs_info(db.Model):
    Student_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Contact = db.Column(db.String(10), nullable=False)
    Email = db.Column(db.String(120), nullable=False)
    Password = db.Column(db.String(120), nullable=False)
    Field_of_interest = db.Column(db.String(120), nullable=False)
    Current_Mentor = db.Column(db.String(120), nullable=True)
    Achievement = db.Column(db.String(120), nullable=True)
    Paper_published = db.Column(db.String(120), nullable=True)
'''
class Supervisor(db.Model):
    Supervisor_ID = db.Column(db.String(50), nullable=False)
    Name = db.Column(db.String(80), nullable=False)
    Contact = db.Column(db.String(10), nullable=False)
    Email = db.Column(db.String(120), nullable=False)
    Password = db.Column(db.String(120), nullable=False)
    Field_of_interest = db.Column(db.String(120), nullable=False)
    On_going_work = db.Column(db.String(120), nullable=True)
    Achievement = db.Column(db.String(120), nullable=True)
    RS_accepted = db.Column(db.String(120), nullable=True)'''
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forum')
def forum():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        Student_ID = request.form.get('Student_ID')
        Password = request.form.get('Password')

        try:
            data = Rs_info.query.filter_by(Student_ID=Student_ID, Password=Password).first()
            if data is not None:
                session['logged_in'] = True
        except:
            return redirect(url_for('home1'))
    return render_template('login.html')

@app.route('/login2')
def login2():
    return render_template('login2.html')

@app.route('/register', methods = ['GET','POST'])
def register():
   if (request.method == 'POST'):
        Name = request.form.get('Name')
        Contact = request.form.get('Contact')
        Email = request.form.get('Email')
        Password = request.form.get('Password')
        Field_of_interest = request.form.get('Field_of_interest')
        Current_Mentor = request.form.get('Current_Mentor')

        entry = Rs_info(Name = Name,Contact = Contact,Email = Email,Password = Password,Field_of_interest = Field_of_interest,Current_Mentor = Current_Mentor)
        db.session.add(entry)
        db.session.commit()
   return render_template('register.html')
@app.route('/register2', methods = ['GET','POST'])
def register2():
    if (request.method == 'POST'):
        Supervisor_ID = request.form.get('Supervisor_ID')
        Name = request.form.get('Name')
        Contact = request.form('Contact')
        Email = request.form.get('Email')
        Password = request.form.get('Password')
        Field_of_interest = request.form.get('Field_of_interest')

        #entry = Supervisor(Supervisor_ID = Supervisor_ID,Name = Name,Contact = Contact,Email = Email,Password = Password,Field_of_interest = Field_of_interest)
       # db.session.add(entry)
        db.session.commit()
    return render_template('register2.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/forum1')
def forum1():
    return render_template('forum1.html')

@app.route('/sbforum1')
def sbforum1():
    return render_template('sbforum1.html')

@app.route('/sbforum2')
def sbforum2():
    return render_template('sbforum2.html')

@app.route('/forum2')
def forum2():
    return render_template('forum2.html')

@app.route('/sbforum3')
def sbforum3():
    return render_template('sbforum3.html')

@app.route('/sbforum4') 
def sbforum4():
    return render_template('sbforum4.html')

@app.route('/forum3')
def forum3():
    return render_template('forum3.html')

@app.route('/sbforum5')
def sbforum5():
    return render_template('sbforum5.html')

@app.route('/sbforum6')
def sbforum6():
    return render_template('sbforum6.html')

@app.route('/forum4')
def forum4():
    return render_template('forum4.html')

@app.route('/profile1')
def profile1():
    return render_template('profile1.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/home1')
def home1():
    return render_template('home1.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')







if __name__ == '__main__':
    app.run(debug = True)