from os import getcwd, path, remove, environ,listdir
import random
from telnetlib import STATUS
from flask import request, jsonify,send_from_directory
from werkzeug.utils import secure_filename
from app import app,mongo
from flask_cors import cross_origin
import time 


from datetime import datetime


#now = datetime.now()
#codigo1 = str(now)
#cadena_codigo = codigo1.replace(':','').replace('-','').replace(' ','')


ROOT_PATH = environ.get('ROOT_PATH')


ALLOWED_EXTENSIONS = set(["xlsx","csv"])

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

app.config["UPLOAD_FOLDER"]="./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads"

path_file_muestra = getcwd() + "./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads/"
path_file = getcwd() + "/modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/images/"
path_file_modelo = getcwd() + "/modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/docs/modeloBin/"



#SUBIR ARCHIVO MUESTRA
@cross_origin
@app.route('/upload', methods = ['POST'])
def upload():
    try:
        file = request.files["myFile"]
        #print(file,file.filename)

        filename = secure_filename(file.filename)
        if file and allowed_file(filename):
            file.save(path.join(app.config["UPLOAD_FOLDER"],filename))        
        return jsonify({"transaccion":True,"message":"Archivo subido con éxito"})
        
    except FileNotFoundError:
        return jsonify({"transaccion":False,"message":"Archivo no se subio, hubo un error"})
    



# GET IMAGEN 
@cross_origin
@app.route("/images/<string:name_file>",methods = ['GET'])
def get_file(name_file):
    return send_from_directory(path_file,path=name_file,as_attachment=False)


# DOWNLOAD IMAGE
@cross_origin
@app.route("/images/download/<string:name_file>",methods = ['GET'])
def download_file(name_file):
    return send_from_directory(path_file,path=name_file,as_attachment=True)

# DELETE IMAGE
@cross_origin
@app.route("/images/delete", methods = ['DELETE'])
def delete_file():
    filename = request.form['filename']
    if path.isfile(path_file + filename ) == False:
        print(path_file + filename )
        return jsonify({"message":"Archivo no encontrado"})
    else:
        try:
            remove(path_file+filename)
            return jsonify({"message":"Archivo borrado"})
        except OSError:
            return jsonify({"ERROR":OSError,"status":"404"})

    

# GET DIRECTORIO MODELOS
@cross_origin
@app.route('/files/directorio-modelo', methods = ['GET'])
def get_directorio_modelo():
    
    contenido = listdir(path_file_modelo)
    modelos = []
    n=1
    
    for fichero in contenido:
        if path.isfile(path.join(path_file_modelo, fichero)) and fichero.endswith('.h5'):
            ti_c = path.getctime(path_file_modelo+fichero)
            c_ti = time.ctime(ti_c)
            ti_m = path.getmtime(path_file_modelo+fichero)
            u_ti = time.ctime(ti_m)
            size = path.getsize(path_file_modelo+fichero)
            modelodic = {'ord':n,'nombre':fichero,'fechaC':c_ti,'fechaU':u_ti,'size':size}
            modelos.append(modelodic)
            n+=1  
    return jsonify({"data":modelos})

# GET DIRECTORIO MUESTRAS 
@cross_origin
@app.route('/files/directorio-muestra', methods = ['GET'])
def get_directorio_muestra():
    
    contenido = listdir(path_file_muestra)
    muestras = []
    n=1
    
    for fichero in contenido:
        if path.isfile(path.join(path_file_muestra, fichero)) and fichero.endswith('.csv'):
            ti_c = path.getctime(path_file_muestra+fichero)
            c_ti = time.ctime(ti_c)
            ti_m = path.getmtime(path_file_muestra+fichero)
            u_ti = time.ctime(ti_m)
            size = path.getsize(path_file_muestra+fichero)
            modelodic = {'ord':n,'nombre':fichero,'fechaC':c_ti,'fechaU':u_ti,'size':size}
            muestras.append(modelodic)
            n+=1  
    return jsonify({"data":muestras})

#  GET DIRECTORIO DE IMAGENER
@cross_origin
@app.route('/files/directorio-images', methods = ['GET'])
def get_directorio():
    contenido = listdir(path_file)
    imagenes = []
    n=1
    for fichero in contenido:
        if path.isfile(path.join(path_file, fichero)) and fichero.endswith('.jpg'):
            ti_c = path.getctime(path_file+fichero)
            c_ti = time.ctime(ti_c)
            ti_m = path.getmtime(path_file+fichero)
            u_ti = time.ctime(ti_m)
            size = path.getsize(path_file+fichero)
            modelodic = {'ord':n,'nombre':fichero,'fechaC':c_ti,'fechaU':u_ti,'size':size}
            imagenes.append(modelodic)
            n+=1  
             
    return jsonify({"data":imagenes})

# GET MODELO 
@cross_origin
@app.route("/modelo/<string:name_file>",methods = ['GET'])
def get_modelo(name_file):
    return send_from_directory(path_file_modelo,path=name_file,as_attachment=False)

