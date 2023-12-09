from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from wtforms import StringField, SubmitField
import pandas as pd
import seaborn as sns
from joblib import dump, load
from sklearn.linear_model import LinearRegression, LogisticRegression


lm_model = load('mpg_model.sav')
df = sns.load_dataset("mpg")
df.head()

df.drop(['name'], axis=1, inplace=True)

df.head()

another_dict = {'cylinders': 4, 'horsepower': 147, 'weight': 1870, 'age': 3, 'origin_japan':0, 'origin_usa':0}
ex_df = pd.DataFrame(another_dict, index=[0])
my_mpg = lm_model.predict(ex_df)
print(my_mpg)

# df.dropna(inplace=True)
#
# X = df.drop(['mpg'], axis=1)
# y = df['mpg']
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 88)
# print(lm_model.score(X_test, y_test))
# print(X_train, X_test)
# print(y_train, y_test)