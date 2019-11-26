from flask import Flask, render_template, request

app = Flask(__name__)

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
def index():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


# to run using python3 flaskblog.py instead of FLASK_DEBUG=1, flask run
if __name__ == '__main__':
    app.run(debug=True)
