import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import numpy as np
from joblib import load

# instanciar objeto Flask
app = Flask(__name__)

# api
api = Api(app)

# carregar arquivos
model = load('model/tree_model.joblib')

class TitanicSurvival(Resource):
    def get(self):
        return {'Nome': 'Byron'}

    def post(self):
        args = request.get_json(force=True)
        input_values = np.asarray(list(args.values())).reshape(1, -1)

        print(args)
        print(input_values)

        predict = model.predict(input_values)

        return jsonify({'Sobrevivencia': int(predict)})

api.add_resource(TitanicSurvival, '/')

if __name__ == '__main__':
    app.run()
