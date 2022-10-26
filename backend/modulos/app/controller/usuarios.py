import os
from flask import request, jsonify
from app import app,mongo
from flask_cors import cross_origin

ROOT_PATH = os.environ.get('ROOT_PATH')

@cross_origin
@app.route('/usuarios/listar-usuarios', methods = ['GET'])
def listar_usuarios():
    if request.method == 'GET':
        data = mongo.db.users.find({})
        listado_documentos = list(data)

        if data == None:
            data = []
        return jsonify({"transaccion":True,"data":listado_documentos})

@app.route('/usuarios/crear-usuario', methods = ['POST'])
def crear_usuario():
    data = request.get_json()
    guardar = mongo.db.users.insert_one(data)
    return jsonify({"transaccion":True,"mensaje":"los datos se almacenaron exitosamente"})