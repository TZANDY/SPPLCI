import os
from flask import request, jsonify, Response
from app import app,mongo
from flask_cors import cross_origin,CORS
from datetime import datetime
from model.Clases._requeriment import Requeriment

ROOT_PATH = os.environ.get('ROOT_PATH')

@cross_origin
@app.route('/requerimiento/listar-requerimiento', methods = ['GET'])
def listar_requerimientos():
    if request.method == 'GET':
        requeriments = mongo.db['requeriments']
        data = mongo.db.requeriments.find({})
        listado_documentos = list(data)
        if data == None:
            data = []
        return jsonify({"transaccion":True,"data":listado_documentos})

#CREAR REQUERIMIENTO
@cross_origin
@app.route('/requerimiento/crear-requerimiento', methods = ['POST'])
def crear_requerimiento():
    requeriments = mongo.db['requeriments']

    nombreInsumo=request.form["nombreInsumo"]
    categoriaInsumo=request.form['categoriaInsumo']
    fecha=request.form['fecha']
    cantidad=request.form['cantidad']
    unidad=request.form['unidad']
    email=request.form['email']
    monto=request.form['monto']
    comentario=request.form['comentario']
    estado=request.form['estado']
    CreateAt=datetime.now()

    if nombreInsumo and categoriaInsumo and fecha and cantidad and unidad and email and monto and comentario and estado and CreateAt:
        requeriment = Requeriment(nombreInsumo,categoriaInsumo,fecha,cantidad,unidad,email,monto , comentario , estado , CreateAt)
        requeriments.insert_one(requeriment.toDBCollection())
        return jsonify({'nombreInsumo':nombreInsumo,'categoriaInsumo':categoriaInsumo,'fecha':fecha,'cantidad':cantidad,'unidad':unidad,'email':email,'monto':monto,'comentario':comentario,'estado':estado,'CreateAt':CreateAt})
    else:
        return notFound()

#CREAR REQUERIMIENTO 2
@cross_origin
@app.route('/requerimiento/crear-requerimiento2', methods = ['POST'])
def crear_requerimiento2():
    #requeriments = mongo.db['requeriments']
    data = request.get_json()
    guardar = mongo.db.requeriments.insert_one(data)
    return jsonify({"transaccion":True,"mensaje":"los datos se almacenaron exitosamente"})

@app.errorhandler(404)
def notFound():
    message = {
        'message':'No encontrado'+request.url,
        'status':'404'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#BORRAR REQUERIMIENTO
@cross_origin
@app.route('/requerimiento/delete/<string:nombreInsumo>', methods = ['DELETE'])
def borrar_requerimiento(nombreInsumo):
    requeriments = mongo.db['requeriments']
    requeriments.delete_one({'nombreInsumo':nombreInsumo})
    return jsonify({"transaccion":True,"mensaje":"los datos se borraron exitosamente"})

#ACTUALIZAR METODOS
@cross_origin
@app.route('/requerimiento/delete/<string:nombreInsumo>', methods = ['DELETE'])
def editar_requerimiento(nombreInsumo):
    requeriments = mongo.db['requeriments']

    nombreInsumo=request.form['nombreInsumo']
    categoriaInsumo=request.form['categoriaInsumo']
    fecha=request.form['fecha']
    cantidad=request.form['cantidad']
    unidad=request.form['unidad']
    email=request.form['email']
    monto=request.form['monto']
    comentario=request.form['comentario']
    estado=request.form['estado']
    CreateAt=datetime.now()

    if nombreInsumo and categoriaInsumo and fecha and cantidad and unidad and email and monto and comentario and estado and CreateAt:
        requeriments.update_one({'nombreInsumo':nombreInsumo},{'$set':{'nombreInsumo':nombreInsumo,'categoriaInsumo':categoriaInsumo,'fecha':fecha,'cantidad':cantidad,'unidad':unidad,'email':email,'monto':monto,'comentario':comentario,'estado':estado,'CreateAt':CreateAt}})
        response = jsonify({'message':'Requerimiento '+nombreInsumo+' actualizado correctamente'})
    else:
        return notFound()