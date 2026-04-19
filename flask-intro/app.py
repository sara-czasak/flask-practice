from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    skills = ['Python', 'Flask', 'JavaScript', 'HTML', 'CSS']
    return render_template('index.html', page_title='Flask 101', skills=skills, is_logged_in=False)


@app.route('/about')
def about():
    return '<h1>About</h1>'


@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello {name.title()}</h1>'