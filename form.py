from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression

class MpgForm(FlaskForm):
    horsepower = StringField("Horsepower")
    cylinders = StringField("Cylinders")
    weight = StringField("Weight")
    modelyear = StringField("ModelYear")
    submit = SubmitField("Submit")

class DiaForm(FlaskForm):
    age = StringField("age")
    bmi = StringField("bmi")
    glucose = StringField("glucose")
    submit = SubmitField("Submit")