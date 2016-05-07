from flask import Flask, redirect, render_template, session, flash, request, url_for
app = Flask(__name__)
app.secret_key = "thisismysecretkey"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjaPage():
	return render_template('ninjas.html' , pagename='all-turtles')
@app.route('/ninja/<pagename>')
def showChosenNinja(pagename):
	return render_template('ninjas.html', pagename=pagename)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

app.run(debug=True)