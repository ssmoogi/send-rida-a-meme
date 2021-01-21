from flask import Flask, escape, render_template, request, url_for
from random import choice
import config

web_site = Flask(__name__)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/verify/', defaults={'password': None})
@web_site.route('/verify/<password>')
def verify(password):
	if not password:
		password = request.args.get('password')

	if not password:
		return 'Wrong password! Please leave.'

	if password == ENTER_KEY:
		return render_template('personal_user.html', user=password)

@web_site.route('/page')
def random_page():
  return render_template('page.html', code=choice(number_list))

web_site.run(host='0.0.0.0', port=8080)