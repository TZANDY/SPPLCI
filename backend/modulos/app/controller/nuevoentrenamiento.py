import os
from flask import request, jsonify
from app import app,mongo
from flask_cors import cross_origin
import shutil
from datetime import datetime
import json
import numpy as np

from modulos.model.MachineLearning.Regression import learningVenta



ROOT_PATH = os.environ.get('ROOT_PATH')



path_file_muestra = os.getcwd() + "/modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads/"



@cross_origin
@app.route('/entrenamiento/nuevo-entrenamiento', methods = ['GET'])
def entrenar():
    #learningVenta.main()
    from modulos.model.MachineLearning.NeuralNets.NeuralNetwork import ann_lstm1
    ann_lstm1.main()
    resultados()
    return jsonify({"transaccion":True,"message":"Entrenamiento exitoso"})

#guardar copia
@cross_origin
@app.route('/files/new-training', methods = ['GET','POST'])
def new_copy_files():
    now = datetime.now()
    codigo1 = str(now)
    cadena_codigo = codigo1.replace(':','').replace('-','').replace(' ','')
    try:
        filename = 'test.xlsx'
        shutil.copy(path_file_muestra+filename,path_file_muestra+str(cadena_codigo[0:14])+"-"+filename)
        if os.path.isfile(path_file_muestra + filename ) == False:
            return jsonify({"message":"Archivo no encontrado"})
        else:
            try:
                os.remove(path_file_muestra+filename)
                return jsonify({'status':'200'})
            except OSError:
                return jsonify({"ERROR":OSError,"status":"404"})
        #shutil.copy('./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads/'+filename,'./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/docs/'+filename)
    except:
        return jsonify({"status":"404"}) 


def resultados():
    from modulos.model.MachineLearning.NeuralNets.NeuralNetwork import ann_lstm1
    resultado = ann_lstm1.dato()
    for fila in resultado:
        for columna in fila:
            print(columna)
    #return json.dumps({'res':arr},cls=MyEncoder)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.str_):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

#def dato():
    #resultado = {"res":cont}
#    arr = []
#    for fila in prediccion:
#        for columna in fila:
#            arr = np.array(float(columna))
            
        
    #print(prediccion[[0][0]])
    #print(arr[1])
    #arr = np.array(resultado)
    
    
    #json_str = json.dumps({'res':arr},cls=NpEncoder)
    #return json_str
#    return json.dumps({'res':arr},cls=MyEncoder)  