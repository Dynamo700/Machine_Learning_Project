from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, FloatField, IntegerField
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression

class MpgForm(FlaskForm):
    horsepower = IntegerField("Horsepower")
    cylinders = IntegerField("Cylinders")
    weight = FloatField("Weight")
    modelyear = IntegerField("ModelYear")
    submit = SubmitField("Submit")

class DiaForm(FlaskForm):
    Age = IntegerField("age")
    BMI = FloatField("bmi")
    Glucose = IntegerField("glucose")
    BloodPressure = FloatField("bloodpressure")
    DiabetesPedigreeFunction = IntegerField("diabetespedigreefunction")
    Pregnancies = IntegerField("Pregnancies")
    submit = SubmitField("Submit")