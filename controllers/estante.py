from flask_restful import Resource, reqparse
from models.estante import EstanteModel

# @app.route("/estante", methods=['get','post'])

class EstantesController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "capacidad",
        type=int,
        required=True,
        help="Capacidad es obligatorio"
    )
    parser.add_argument(
        "ubicacion",
        type=str,
        required=True,
        help="Ubicacion es obligatorio"
    )
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Descripcion es obligatorio"
    )
    parser.add_argument(
        "estado",
        type=bool,
        required=True,
        help="Estado es obligatorio"
    )

    def get(self):
        estantes = EstanteModel.query.all()
        resultado = []
        for estante in estantes:
            # print(estante)
            libros=[]
            # resultado.append(estante.mostrar_json())
            for libro in estante.libros:
                # print(libro.mostrar_json())
                libros.append(libro.mostrar_json())
            temporal = estante.mostrar_json()
            temporal['libros'] = libros
            resultado.append(temporal)

        print(resultado)

        return{
            'ok': True,
            'message': None,
            'content': resultado
        }

    def post(self):
        data = self.parser.parse_args()
        estante = EstanteModel(data['capacidad'], data['ubicacion'], data['descripcion'], data['estado'])
        try:
            estante.save()
            return{
                'ok': True,
                'message': 'Correcto',
                'content': estante.mostrar_json()
            }
        except:
            return{
                'ok': False,
                'message': 'Ocurrió un error',
                'content': None
            },500


class EstanteController(Resource):
    def get(self, est_id):
        estante = EstanteModel.query.filter_by(id=est_id).first()
        print(estante)

        if estante:
            return{
                'ok' : True,
                'message': 'Todo bien',
                'content' : estante.mostrar_json()
            }
        else:
            return{
                'ok' : False,
                'message': 'No existe estante con id:' + str(est_id),
                'content' : ''
            }

    def delete(self, est_id):
        estante = EstanteModel.query.filter_by(id=est_id).first()
        if estante:
            if estante.estado:
                estante.estado = False
                estante.save() 
                return{
                    'ok' : True,
                    'message': 'Se inhabilito exitosamente el estante',
                    'content' : estante.mostrar_json()
                }
            else:
                return{
                    'ok' : False,
                    'message': 'El estante ya se encuentra deshabilitado',
                    'content' : None
                }
        else:
            return{
                'ok' : False,
                'message': 'No existe estante con id:' + str(est_id),
                'content' : ''
            }

    def put(self, est_id):
        estante = EstanteModel.query.filter_by(id=est_id).first()
        if estante:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "capacidad",
                type=int,
                required=True,
                help="Capacidad es obligatorio"
            )
            parser.add_argument(
                "ubicacion",
                type=str,
                required=True,
                help="Ubicacion es obligatorio"
            )
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Descripcion es obligatorio"
            )
            parser.add_argument(
                "estado",
                type=bool,
                required=True,
                help="Estado es obligatorio"
            )

            data = parser.parse_args()    

            estante.capacidad= data['capacidad']
            estante.ubicacion= data['ubicacion']
            estante.descripcion= data['descripcion']
            estante.estado = data['estado']
            estante.save() 

            return{
                'ok' : True,
                'message': 'Todo bien',
                'content' : estante.mostrar_json()
            }  
        else:
            return{
                'ok' : False,
                'message': 'No existe estante con id:' + str(est_id),
                'content' : ''
            }