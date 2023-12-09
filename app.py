from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression, LogisticRegression
from form import MpgForm, DiaForm


app = Flask(__name__)
app.config['SECRET_KEY']='WtVxifd"zZKpMvBv:&Oc1D-Eh9H23GN'
lm_model = load('mpg_model.sav')
logr_model = load('diabetes_model.sav')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/mpg", methods=['GET', 'POST'])
def formPageMpg():
    nameForm1 = MpgForm()

    if(request.method == "POST" and nameForm1.is_submitted()):
        print("submitted")
        hp = int (nameForm1.horsepower.data)
        cy = int (nameForm1.cylinders.data)
        wt = int(nameForm1.weight.data)
        my = int(nameForm1.modelyear.data)
        print(hp)
        print(cy)
        print(wt)
        print(my)
        print(lm_model)

        another_dict = {'cylinders': cy, 'horsepower': hp, 'weight': wt, 'age': 2023 - my, 'origin_japan': 0, 'origin_usa': 0}
        ex_df = pd.DataFrame(another_dict, index=[0])
        my_mpg = lm_model.predict(ex_df)
        print(my_mpg)



    return render_template("index.html", form=nameForm1)



@app.route("/diabetesForm", methods=['GET', 'POST'])
def formPageDia():
    nameForm2 = DiaForm()

    if(request.method == "POST" and nameForm2.is_submitted()):
        print("submitted")
        ag = nameForm2.age.data
        bm = nameForm2.bmi.data
        gl = nameForm2.glucose.data
        print(ag)
        print(bm)
        print(gl)
        print(logr_model)



    return render_template("diabetes.html", form=nameForm2)


if __name__ == '__main__':
    app.run(debug=True)