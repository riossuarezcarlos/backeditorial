from flask import Flask
# https://flask-restful.readthedocs.io/en/latest/installation.html
from flask_restful import Api
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
from base_datos import db

from models.estante import EstanteModel
from models.autor import AutorModel
from models.libro import LibroModel
from models.autorlibro import AutorLibroModel

from controllers.estante import EstantesController, EstanteController
from controllers.libro import LibrosController, LibroController, EncontrarLibroController

app = Flask(__name__)
# dialect+driver://username:password@host:port/database

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://fe4uey0rfcuzw5xb:dn9e5bn1vb7v0ixq@f2fbe0zvg9j8p9ng.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/ndz0d4fmmgurl6g0'

api = Api(app=app)

@app.before_first_request
def iniciador():
    #Aquí se conecta al servidor
    db.init_app(app)
    #eliminación de los modelos
    # db.drop_all(app=app)
    #Creación de los Modelos
    db.create_all(app=app)


@app.route('/')
def inicio():
    return 'El servidor funciona correctamente'


# Definir las rutas
api.add_resource(EstantesController, '/estante')
api.add_resource(EstanteController, '/estante/<int:est_id>')
api.add_resource(LibrosController, '/libro')
api.add_resource(LibroController, '/libro/<int:libro_id>')
api.add_resource(EncontrarLibroController, '/libro/<string:palabra>')


if __name__ == '__main__':
    app.run(debug=True)