from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User_Agent')
#     return '<h1>Hello, {}</h1>'.format(user_agent)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)