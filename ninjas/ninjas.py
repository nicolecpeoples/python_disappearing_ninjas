from flask import Flask, redirect, render_template, session, flash, request, url_for
app = Flask(__name__)
app.secret_key = "thisismysecretkey"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def allninjas():
	return render_template('ninjas.html')

@app.route('/ninja/orange')
def orangeNinja():
	return render_template('orange.html')

@app.route('/ninja/purple')
def purpleNinja():
		return render_template('purple.html')

@app.route('/ninja/blue')
def blueNinja():
	return render_template('blue.html')

@app.route('/ninja/red')
def redninja():
		return render_template('red.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

app.run(debug=True)