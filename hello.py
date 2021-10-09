from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
# @app.route('/')
# def index():
#     user_agent = request.headers.get('User_Agent')
#     return '<h1>Hello, {}</h1>'.format(user_agent)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)