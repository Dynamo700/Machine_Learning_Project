from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField

app = Flask(__name__)

class MyForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/form")
def formPage():
    return render_template("index.html")