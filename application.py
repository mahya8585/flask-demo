from flask import Flask
from flask import request
import flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/hello/jp')
def greeting():
    return 'こんにちは！'


@app.route('/greeting/<string:user_name>')
def greeting_user(user_name):
    return '{uname}さん、さようなら！'.format(uname=user_name)


@app.route('/greeting')
def greeting_name():
    user = request.args.get('user')
    return '{uname}さん、疲れてる？'.format(uname=user)


@app.route('/welcome/<string:user_name>')
def welcome_index(user_name):
    return flask.render_template(
        'index.html',
        name=user_name
    )


@app.route('/echo', methods=['POST'])
def echo():
    echo_word = request.form['input_word']
    return flask.render_template(
        'echo.html',
        echo=echo_word
    )