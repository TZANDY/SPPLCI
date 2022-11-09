import os
from flask import request, jsonify, Response
from app import app,mongo
from flask_cors import cross_origin,CORS
from datetime import datetime
from model.Clases._requeriment import Requeriment,CustomEncoder
from bson.objectid import ObjectId



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


#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *

#CREAR REQUERIMIENTO
@cross_origin
@app.route('/requerimiento/crear-requerimiento', methods = ['POST'])
def crear_requerimiento():
    requeriment = mongo.db['requeriments']

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
        requeriment = Requeriment(nombreInsumo,categoriaInsumo,fecha,cantidad,unidad,email,monto , comentario , estado , CreateAt)
        requeriment.insert_one(requeriment.toDBCollection())
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


#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *

@app.errorhandler(404)
def notFound():
    message = {
        'message':'No encontrado'+request.url,
        'status':'404'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *

#BORRAR REQUERIMIENTO
@cross_origin
@app.route('/requerimiento/delete/<string:_id>', methods = ['DELETE'])
def borrar_requerimiento(_id):
    requeriments = mongo.db['requeriments']
    idBuscar={"_id":ObjectId(_id)}
    requeriments.delete_one(idBuscar)
    return jsonify({"transaccion":True,"mensaje":"los datos se borraron exitosamente"})

#BORRAR REQUERIMIENTO 2
#@cross_origin
#@app.route('/requerimiento/delete2/<string:nombreInsumo>', methods = ['DELETE'])
#def borrar_requerimiento2(nombreInsumo):
#    guardar = mongo.db.requeriments.delete_one({'nombreInsumo':nombreInsumo})
#    return jsonify({"transaccion":True,"mensaje":"los datos se almacenaron exitosamente"})


#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *

#ACTUALIZAR METODOS
@cross_origin
@app.route('/requerimiento/update/<string:_id>', methods =['PUT'])
def editar_requerimiento(_id):
    #requeriments = mongo.db['requeriments']
    requeriments = request.get_json(force=True)
    idBuscar={"_id":ObjectId(_id)}

    #_id=requeriments['_id']
    nombreInsumo=requeriments['nombreInsumo']
    categoriaInsumo=requeriments['categoriaInsumo']
    fecha=requeriments['fecha']
    cantidad=requeriments['cantidad']
    unidad=requeriments['unidad']
    email=requeriments['email']
    monto=requeriments['monto']
    comentario=requeriments['comentario']
    estado=requeriments['estado']

    print(_id)
    
    if nombreInsumo and categoriaInsumo and fecha and cantidad and unidad and email and monto and comentario and estado:
        requeriment = Requeriment(nombreInsumo,categoriaInsumo,fecha,cantidad,unidad,email,monto ,estado,comentario)
        #print(requeriment.)
        mongo.db.requeriments.update_one(idBuscar,{'$set':{"nombreInsumo":requeriment.nombreInsumo,"categoriaInsumo":requeriment.categoriaInsumo,"fecha":requeriment.fecha,"cantidad":requeriment.cantidad,"unidad":requeriment.unidad,"email":requeriment.email,"monto":requeriment.monto,"comentario":requeriment.comentario,"estado":requeriment.estado}})
        #mongo.db.requeriments.update_one({"_id":idBuscar},{'$set':{"nombreInsumo":requeriment.nombreInsumo,"categoriaInsumo":requeriment.categoriaInsumo,"fecha":requeriment.fecha,"cantidad":requeriment.cantidad,"unidad":requeriment.unidad,"email":requeriment.email,"monto":requeriment.monto,"comentario":requeriment.comentario,"estado":requeriment.estado}})
        #requeriments.update_one({'nombreInsumo':nombreInsumo},{'$set':{'nombreInsumo':nombreInsumo,'categoriaInsumo':categoriaInsumo,'fecha':fecha,'cantidad':cantidad,'unidad':unidad,'email':email,'monto':monto,'comentario':comentario,'estado':estado}})
        return jsonify({'message':'Requerimiento '+nombreInsumo+' actualizado correctamente'})
    else:
        return notFound()

#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
#*  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  *   *   *   *   *   *   *   *   *   *   *   *   *   *
