from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, FloatField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression

class MpgForm(FlaskForm):
    horsepower = DecimalField("Horsepower", validators=[DataRequired()])
    cylinders = IntegerField("Cylinders", validators=[DataRequired()])
    weight = FloatField("Weight", validators=[DataRequired()])
    modelyear = IntegerField("ModelYear", validators=[DataRequired()])
    origin_usa = IntegerField("Origin_usa", validators=[DataRequired()])
    origin_japan = IntegerField("Origin_japan", validators=[DataRequired()])
    origin_europe = IntegerField("Origin_europe", validators=[DataRequired()])
    submit = SubmitField("Submit")

class DiaForm(FlaskForm):
    Age = IntegerField("age", validators=[DataRequired()])
    BMI = FloatField("bmi", validators=[DataRequired()])
    Glucose = IntegerField("glucose", validators=[DataRequired()])
    BloodPressure = FloatField("bloodpressure", validators=[DataRequired()])
    DiabetesPedigreeFunction = IntegerField("diabetespedigreefunction", validators=[DataRequired()])
    Pregnancies = IntegerField("Pregnancies", validators=[DataRequired()])
    submit = SubmitField("Submit")