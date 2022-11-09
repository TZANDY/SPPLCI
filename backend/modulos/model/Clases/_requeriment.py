import json


class Requeriment:
    def __init__(self,nombreInsumo,categoriaInsumo,fecha,cantidad,unidad,email,monto,estado,comentario):
        
        self.nombreInsumo=nombreInsumo
        self.categoriaInsumo=categoriaInsumo
        self.fecha=fecha
        self.cantidad=cantidad
        self.unidad=unidad
        self.email=email
        self.monto=monto
        self.estado=estado
        self.comentario=comentario
        

    def toDBCollection(self):
        return{
            
            'nombreInsumo':self.nombreInsumo,
            'categoriaInsumo':self.categoriaInsumo,
            'fecha':self.fecha,
            'cantidad':self.cantidad,
            'unidad':self.unidad,
            'email':self.email,
            'monto':self.monto,
            'estado':self.estado,
            'comentario':self.comentario
            
        }
    
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

    