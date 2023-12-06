from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField
from joblib import dump, load
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
app.config['SECRET_KEY']='my_secret_key'

class MyForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/form", methods=['GET', 'POST'])
def formPage():
    nameForm = MyForm()

    if(request.method == "POST" and nameForm.is_submitted()):
        nameInputData = nameForm.name.data
        print("submitted")
        print(nameInputData)


    return render_template("index.html", form=nameForm)