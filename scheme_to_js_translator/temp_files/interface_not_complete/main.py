from flask import Flask, render_template, session, redirect, request, url_for, g, flash, abort
import os

app = Flask(__name__)
SECRET_KEY = "You are my compiler. My life wouldn't start without you."
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template('scheme.html') 

@app.route('/scheme', methods=['GET','POST'])
def input_scheme():
	code = request.form['scheme_code']	 
	js_code = code#"translated scheme_code to js_code"
	return render_template("js.html", js_code = js_code)

if __name__== "__main__":
	app.run(debug=True)
