from flask import Flask, render_template,request
import numpy as np
import picklei
import pandas as pd

model - pickle.load(open(r"model1.pkl"'rb'))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/predict")
def pred():
    return render_template('predict.html')


@app.route("/pred",methods=['POST,GET'])
def predict():
    x = [[int(x) for x in request.form.value()]]
    print(x)

    x= np.array(x)
    print(x.shape)


    print(x)
    pred = model.predict(x)
    print(pred[0])
    return render_template('submit.html',prediction_text=pred[0])


if __name__=="__main":
    app.run(debug=False)