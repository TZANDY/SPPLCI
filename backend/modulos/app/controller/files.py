from os import getcwd, path, remove, environ,listdir
import random
from telnetlib import STATUS
from flask import request, jsonify,send_from_directory
from werkzeug.utils import secure_filename
from app import app,mongo
from flask_cors import cross_origin


from datetime import datetime


now = datetime.now()
codigo1 = str(now)
cadena_codigo = codigo1.replace(':','').replace('-','').replace(' ','')


ROOT_PATH = environ.get('ROOT_PATH')


ALLOWED_EXTENSIONS = set(["xlsx","csv"])

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

app.config["UPLOAD_FOLDER"]="./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads"

path_file = getcwd() + "/modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/images/"


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
    

# LISTAR ARCHIVOS DEL DIRECTORIO
@cross_origin
@app.route('/files/directorio-images', methods = ['GET'])
def get_directorio():
    contenido = listdir(path_file)
    imagenes = []
    for fichero in contenido:
        if path.isfile(path.join(path_file, fichero)) and fichero.endswith('.jpg'):
            imagenes.append(fichero)
             
    return jsonify({"data":imagenes})

#ENVIAR IMAGEN AL NAVEGADOR EL ARCHIVO
@cross_origin
@app.route("/images/<string:name_file>",methods = ['GET'])
def get_file(name_file):
    return send_from_directory(path_file,path=name_file,as_attachment=False)


#DESCARGAR EL ARCHIVO
@cross_origin
@app.route("/images/download/<string:name_file>",methods = ['GET'])
def download_file(name_file):
    return send_from_directory(path_file,path=name_file,as_attachment=True)

#BORRAR EL ARCHIVO
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

    

