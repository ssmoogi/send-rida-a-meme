from flask import Flask, escape, render_template, request, url_for
from random import choice
from config import *
from send_message import *

app = Flask(__name__)

meme_list = ["kait-hi.png", "sahana-lol.jpg", "choir.jpg"]

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/verify/', defaults={'password': None})
@app.route('/verify/<password>')
def verify(password):
	if not password:
		password = request.args.get('password')

	if not password or password != ENTER_KEY:
		return render_template('meme.html', entered=password, password=ENTER_KEY)

	if password == ENTER_KEY:
		return render_template('meme.html', entered=password, password=ENTER_KEY, image=choice(meme_list))

@app.route('/send', defaults={'sender': None, 'message': None, 'meme': None})
@app.route('/send/<sender>/<message>/<meme>')
def send(sender, message, meme):
	if not sender:
		sender = request.args.get('sender')
	if not message:
		message = request.args.get('message')
	if not meme:
		meme = request.args.get('meme')
		meme = 'https://raw.githubusercontent.com/ssmoogi/send-rida-a-meme/master/static/images/memes/' + meme
	
	send_message(sender, message, meme)
	return render_template('sent.html')

#app.run(host='0.0.0.0', port=8080)