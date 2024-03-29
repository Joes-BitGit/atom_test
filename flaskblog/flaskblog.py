from datetime import datetime
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LogInForm

app = Flask(__name__)

# ideally to be random characters
# import secrets
# secrets.token_hex('Number of bytes')
app.config['SECRET_KEY'] = '2960ff25e8605752'
# /// relative path to the current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Joseph Almeida',
        'title': 'Blog Post #1',
        'content': 'First Post content',
        'date_posted': 'November 24, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post #10',
        'content': 'Second Post content',
        'date_posted': 'November 25, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # f-strings are expressions evaluated at runtime rather than constant values
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in as admin!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Login Unsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)


# to run using python3 flaskblog.py instead of FLASK_DEBUG=1, flask run
if __name__ == '__main__':
    app.run(debug=True)
