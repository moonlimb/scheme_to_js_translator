from flask import Flask, render_template, session, redirect, request, url_for, g, flash, abort
import os

app = Flask(__name__)
SECRET_KEY = "You are my compiler. My life wouldn't start without you."
app.config.from_object(__name__)


@app.route("/")
def index():
	return "this is index page"

if __name__== "__main__":
	app.run(debug=True)
