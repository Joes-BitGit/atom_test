from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return '<h2>Home Page!</h2>'

@app.route('/about')
def about():
    return '<h2>About Page!</h2>'


# to run using python3 flaskblog.py instead of FLASK_DEBUG=1, flask run 
if __name__ == '__main__':
    app.run(debug=True)
