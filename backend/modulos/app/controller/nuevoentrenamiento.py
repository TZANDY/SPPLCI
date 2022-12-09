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
path_file_image = os.getcwd()+"/modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/images/"

@cross_origin
@app.route('/entrenamiento/nuevo-entrenamiento', methods = ['GET'])
def entrenar():
    #learningVenta.main()
    from modulos.model.MachineLearning.NeuralNets.NeuralNetwork import ann_lstm1
    ann_lstm1.main()
    resultado = ann_lstm1.obtenerResultados()
    return json.dumps({'res':resultado},cls=MyEncoder)
    #resultados()
    #return jsonify({"transaccion":True,"message":"Entrenamiento exitoso"})

#guardar copia
@cross_origin
@app.route('/files/new-training', methods = ['GET','POST'])
def new_copy_files():
    now = datetime.now()
    codigo1 = str(now)
    cadena_codigo = codigo1.replace(':','').replace('-','').replace(' ','')
    try:
        filename = 'test.csv'
        imagename = 'test.jpg'
        index_val_accuracy='index_val_accuracy.jpg'
        index_val_loss ='index_val_loss.jpg'
        index_loss ='index_loss.jpg'

        shutil.copy(path_file_muestra+filename,path_file_muestra+str(cadena_codigo[0:14])+"-"+filename)
        shutil.copy(path_file_image+imagename,path_file_image+str(cadena_codigo[0:14])+"-"+imagename)
        shutil.copy(path_file_image+index_val_accuracy,path_file_image+str(cadena_codigo[0:14])+"-"+index_val_accuracy)
        shutil.copy(path_file_image+index_val_loss,path_file_image+str(cadena_codigo[0:14])+"-"+index_val_loss)
        shutil.copy(path_file_image+index_loss,path_file_image+str(cadena_codigo[0:14])+"-"+index_loss)
        if os.path.isfile(path_file_muestra + filename ) == False | os.path.isfile(path_file_image + imagename ) == False| os.path.isfile(path_file_image + index_val_accuracy ) == False| os.path.isfile(path_file_image + index_val_loss ) == False| os.path.isfile(path_file_image + index_loss ) == False:
            return jsonify({"message":"Archivo no encontrado"})
        else:
            try:
                os.remove(path_file_muestra+filename)
                os.remove(path_file_image+imagename)
                os.remove(path_file_image+index_val_accuracy)
                os.remove(path_file_image+index_val_loss)
                os.remove(path_file_image+index_loss)
                return jsonify({'status':'200'})
            except OSError:
                return jsonify({"ERROR":OSError,"status":"404"})
        #shutil.copy('./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads/'+filename,'./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/docs/'+filename)
    except:
        return jsonify({"status":"404"}) 

#obtener resultados
@cross_origin
@app.route('/resultados', methods = ['GET'])
def resultados():
    from modulos.model.MachineLearning.NeuralNets.NeuralNetwork import ann_lstm1
    resultado = ann_lstm1.obtenerResultados()
    #return jsonify({"data":resultado})
    return json.dumps({'res':resultado},cls=MyEncoder)

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