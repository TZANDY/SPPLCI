
from flask import Flask
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import datetime
import certifi
from flask_cors import CORS

MONGO_URI='mongodb+srv://main:Gh1t7nEWqY341Cct@cluster0.jpavp0z.mongodb.net/db-name?retryWrites=true&w=majority'

ca = certifi.where()

class JSONEncoder(json.JSONEncoder):
    
    def default(self,o):
        if isinstance(o,ObjectId):
            return str(o)
        if isinstance (o,datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self,o)

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI']=MONGO_URI
app.json_encoder = JSONEncoder
mongo = PyMongo(app)
from app.controller import usuarios,entrenamiento,nuevoentrenamiento

