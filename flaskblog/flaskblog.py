from flask import Flask, render_template, request, url_for, flash, redirect
from forms import RegistrationForm, LogInForm

app = Flask(__name__)

# ideally to be random characters
# import secrets
# secrets.token_hex('Number of bytes')
app.config['SECRET_KEY'] = '2960ff25e8605752'

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

@app.route('/login')
def login():
    form = LogInForm()
    return render_template('login.html', title='Login', form=form)


# to run using python3 flaskblog.py instead of FLASK_DEBUG=1, flask run
if __name__ == '__main__':
    app.run(debug=True)
