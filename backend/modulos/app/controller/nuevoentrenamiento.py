import os
from flask import request, jsonify
from app import app,mongo
from flask_cors import cross_origin

from modulos.model.MachineLearning.Regression import learningVenta
from modulos.model.MachineLearning.NeuralNets.NeuralNetwork import ann_lstm1


ROOT_PATH = os.environ.get('ROOT_PATH')


@cross_origin
@app.route('/entrenamiento/nuevo-entrenamiento', methods = ['GET'])
def entrenar():
    #learningVenta.main()
    ann_lstm1.main()
    return jsonify({"transaccion":True,"message":"Entrenamiento exitoso"})