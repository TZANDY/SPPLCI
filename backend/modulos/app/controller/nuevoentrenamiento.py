import os
from flask import request, jsonify
from app import app,mongo
from flask_cors import cross_origin
import shutil
from datetime import datetime

from modulos.model.MachineLearning.Regression import learningVenta



ROOT_PATH = os.environ.get('ROOT_PATH')



path_file_muestra = os.getcwd() + "/modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads/"



@cross_origin
@app.route('/entrenamiento/nuevo-entrenamiento', methods = ['GET'])
def entrenar():
    #learningVenta.main()
    from modulos.model.MachineLearning.NeuralNets.NeuralNetwork import ann_lstm1
    ann_lstm1.main()
    listadoresultados= list(ann_lstm1.dato())
    return jsonify({"transaccion":True,"message":"Entrenamiento exitoso","data":listadoresultados})

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
