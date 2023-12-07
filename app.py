from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
app.config['SECRET_KEY']='my_secret_key'
lm_model = LinearRegression(), load('mpg_model.joblib')

class MyForm(FlaskForm):
    horsepower = StringField("Horsepower")
    cylinders = StringField("Cylinders")
    weight = StringField("Weight")
    modelyear = StringField("ModelYear")
    submit = SubmitField("Submit")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/form", methods=['GET', 'POST'])
def formPage():
    nameForm = MyForm()

    if(request.method == "POST" and nameForm.is_submitted()):
        print("submitted")
        hp = nameForm.horsepower.data
        cy = nameForm.cylinders.data
        wt = nameForm.weight.data
        my = nameForm.modelyear.data
        print(hp)
        print(cy)
        print(wt)
        print(my)
        print(lm_model)



        # another_dict = {"cylinders": cy, "horsepower": hp, "weight": wt, "modelYear": my}
        # ex_df = pd.DataFrame(another_dict, index=[0])
        # # model.fit(lm_model)
        # my_mpg = lm_model.predict(ex_df)
        # print(my_mpg)



    return render_template("index.html", form=nameForm)