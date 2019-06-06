from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

import pickle

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("hello.html", message="天才")


@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv("text.csv")
    target = df["Category"]
    text = df["Message"]
    vect = CountVectorizer(token_pattern=r"\b\w[\w']+\b",stop_words="english")
    cv_text = vect.fit_transform(text)
    model = RandomForestClassifier()
    model.fit(cv_text, target)
    # pickle.dump(model, open("model.sav", 'wb'))
    # model = pickle.load(open("model.sav",'rb'))


    if request.method == "POST":
        comment = request.form['comment']
        data = [comment]
        vec = vect.transform(data).toarray()
        #print(vec)
        pred = model.predict(vec)




    #     comment2 = request.form['comment2']
    #     data = comment + comment2




    return render_template("result.html", prediction = pred)



if __name__ == '__main__':
    app.run(debug=True)


