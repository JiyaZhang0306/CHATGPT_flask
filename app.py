from flask import Flask, render_template, request
from bot import get_response

app = Flask(__name__)

default_question = "What is your favirot color"

@app.route('/')
def index():
    answer = get_response(default_question)
    return render_template('index.html', color = color_answer, question=default_question, bot_answer=bot_answer)

@app.route('/', methods=['POST'])
def index_post():
    user_question = request.form['req_question']
    answer = get_response(user_question)
    bot_answer = answer.split('-')[0]
    color_answer = answer.split('-')[1]
    return render_template('index.html',  color = color_answer, question=default_question, bot_answer=bot_answer)