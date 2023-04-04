import flask
from flask import render_template, Flask, jsonify, request

import pickle
import pandas as pd


app = Flask(__name__)

 
with open("model_predict.pkl", "rb") as f:
    model = pickle.load(f)
    
with open("model_predict.pkl", "rb") as f:
    model_columns = pickle.load(f)


@app.route('/')
def welcome():
    return "Welcome! Use this Flask App to predict whether a loan will be approved."

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if flask.request.method == 'GET':
        return "Prediction page. Try using post with params to get a prediction."

    if flask.request.method == 'POST':
        try:
            json_ = request.json
            print(json_)
            query_ = pd.DataFrame(json_, index=[0])
            
            prediction = model.predict(query_)
            
            return jsonify({
                "prediction" : str(prediction)
            })
           
        except:
            return jsonify({
                    "trace": traceback.format_exc()
            }) 
    
if __name__ == "__main__":
    app.run()