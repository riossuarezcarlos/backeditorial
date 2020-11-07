from base_datos import db
class LibroModel(db.Model):
    __tablename__= "t_libro"
    id = db.Column("lib_id", db.Integer, primary_key=True)
    nombre = db.Column("lib_nomb",db.String(50))
    editorial = db.Column("lib_editorial",db.String(50))
    numpag = db.Column("lib_numpag",db.Integer)
    precio = db.Column("lib_precio", db.Float())
    publicacion = db.Column("lib_publicacion",db.String(4))
    codigo = db.Column("lib_cod",db.Text)
    estado = db.Column(db.Boolean, default=True)
    # RELACIONES
    est_id = db.Column(db.Integer, db.ForeignKey('t_estante.est_id'), nullable=False)
    
    autores = db.relationship('AutorLibroModel', backref='libro')
    # estante = db.relationship('EstanteModel', backref='libro')

    def __init__(self,nombre, editorial, numpag, precio, publicacion, codigo, estante):
        self.nombre = nombre
        self.editorial = editorial
        self.numpag = numpag
        self.precio = precio
        self.publicacion = publicacion
        self.codigo = codigo
        self.est_id = estante

    def save(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return{
            'id': self.id,
            'nombre': self.nombre,
            'editorial': self.editorial,
            'num_paginas': self.numpag,
            'precio': self.precio,
            'publicacion': self.publicacion,
            'codigo': self.codigo,
            'estante': self.est_id,
            'estado': self.estado
        }

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s'%(self.id,self.nombre,self.editorial,self.numpag,self.precio,self.publicacion,self.codigo,self.est_id, self.estado)