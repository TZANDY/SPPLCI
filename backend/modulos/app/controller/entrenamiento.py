import os
from telnetlib import STATUS
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app import app,mongo
from flask_cors import cross_origin


ROOT_PATH = os.environ.get('ROOT_PATH')


ALLOWED_EXTENSIONS = set(["xlsx","csv"])

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

app.config["UPLOAD_FOLDER"]="./modulos/model/MachineLearning/NeuralNets/NeuralNetwork/public/uploads"




@cross_origin
@app.route('/upload', methods = ['POST'])
def upload():
    
    file = request.files["myFile"]
    #print(file,file.filename)
    filename = secure_filename(file.filename)
    if file and allowed_file(filename):

        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        
        return jsonify({"transaccion":True,"message":"Archivo subido con éxito"})
    return jsonify({"transaccion":False,"message":"Archivo no se subio, hubo un error"})



       