from base_datos import db

class AutorModel(db.Model):
    __tablename__ = 't_autor'
    # automaticamente se designa autoincrementable al primer primary key int
    # para deshabilitar usar autoincremente=False
    id = db.Column("autor_id",db.Integer, primary_key=True)
    nombre = db.Column("autor_nombre",db.String(50))
    estado = db.Column(db.Boolean, default=True)
    libros = db.relationship('AutorLibroModel', backref='autor')

    def __init__(self, nombre):
        self.nombre = nombre 