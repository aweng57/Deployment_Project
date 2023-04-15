
from flask import Flask, jsonify, request


from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

app = Flask(__name__)
api = Api(app)

model = pickle.load( open( "model_predict.pkl", "rb" ))

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        print(json_data)
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        
        res = model.predict_proba(df)
      
        return res.tolist() 

api.add_resource(Scoring, '/scoring')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)
    #app.run(debug=True)