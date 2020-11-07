from flask_restful import Resource, reqparse
from models.libro import LibroModel

class LibrosController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required= True,
        help="nombre es obligatorio"
    )
    parser.add_argument(
        "editorial",
        type=str,
        required= True,
        help="editorial es obligatorio"
    )
    parser.add_argument(
        "num_paginas",
        type=int,
        required= True,
        help="num_paginas es obligatorio"
    )

    parser.add_argument(
        "precio",
        type=float,
        required= True,
        help="precio es obligatorio"
    )
    parser.add_argument(
        "publicacion",
        type=str,
        required= True,
        help="publicacion es obligatorio"
    )
    parser.add_argument(
        "codigo",
        type=str,
        required= True,
        help="codigo es obligatorio"
    )
    parser.add_argument(
        "estante",
        type=int,
        required= True,
        help="estante es obligatorio"
    ) 
   
    def get(self):
        libros = LibroModel.query.all()
        print(libros)
        resultado = []
        for libro in libros:
            print(libro)
            temporal = libro.mostrar_json()
            print(temporal);
            temporal['estante'] = libro.estante.mostrar_json()
            resultado.append(temporal)
            # print(libro.estante.mostrar_json())

        return {
            'ok': True,
            'message': '',
            'content': resultado
        }
    def post(self):
        data = self.parser.parse_args()
        libro = LibroModel(
            data['nombre'],
            data['editorial'],
            data['num_paginas'],
            data['precio'],
            data['publicacion'],
            data['codigo'],
            data['estante']
        )
        try:
            libro.save()
            return{
                'ok': True,
                'message': 'Registrado correctamente',
                'content': libro.mostrar_json()
            }
        except:
            return{
                'ok': False,
                'message': 'Ocurrio un error',
                'content': None
            }


class LibroController(Resource):
    def get(self, libro_id):
        libro = LibroModel.query.filter_by(id=libro_id).first()
        if libro:
            return{
                'ok': True,
                'message': '',
                'content': libro.mostrar_json()
            }
        else:
            return{
                'ok': False,
                'message': 'No existe libro con el id:' + str(libro_id),
                'content': ''
            }
    def put(self, libro_id):
        libro = LibroModel.query.filter_by(id=libro_id).first()
        if libro:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "nombre",
                type=str,
                required= True,
                help="nombre es obligatorio"
            )
            parser.add_argument(
                "editorial",
                type=str,
                required= True,
                help="editorial es obligatorio"
            )
            parser.add_argument(
                "num_paginas",
                type=int,
                required= True,
                help="num_paginas es obligatorio"
            )

            parser.add_argument(
                "precio",
                type=float,
                required= True,
                help="precio es obligatorio"
            )
            parser.add_argument(
                "publicacion",
                type=str,
                required= True,
                help="publicacion es obligatorio"
            )
            parser.add_argument(
                "codigo",
                type=str,
                required= True,
                help="codigo es obligatorio"
            )
            parser.add_argument(
                "estante",
                type=int,
                required= True,
                help="estante es obligatorio"
            ) 
            data = parser.parse_args() 
            libro.nombre = data['nombre']
            libro.editorial = data['editorial']
            libro.num_paginas = data['num_paginas']
            libro.precio = data['precio']
            libro.publicacion = data['publicacion']
            libro.codigo = data['codigo']
            libro.est_id = int(data['estante']) 
            libro.save()

            return{
                'ok': True,
                'message': 'Libro actualizado correctamente',
                'content': libro.mostrar_json()
            }
        else:
            return{
                'ok': False,
                'message': 'No existe libro con el id:' + str(libro_id),
                'content': ''
            }       
    def delete(seld, libro_id):
        libro = LibroModel.query.filter_by(id=libro_id).first()
        if libro:
            if libro.estado:
                libro.estado = False
                libro.save()
                return{
                    'ok': True,
                    'message': 'Se deshabilito correctamente el libro',
                    'content': libro.mostrar_json()
                }
            else:
                return{
                        'ok': True,
                        'message': 'El libro ya se encuentra deshabilitado',
                        'content': ''
                    }
        else:
            return{
                'ok': False,
                'message': 'No existe libro con el id:' + str(libro_id),
                'content': ''
            }

class EncontrarLibroController(Resource):
    def get(self, palabra):
        libros = LibroModel.query.filter(LibroModel.nombre.like('%' + palabra + '%')).all()
        resultado = []
        for libro in libros:
            resultado.append(libro.mostrar_json())

        return{
            'ok': True,
            'message': '',
            'content': resultado
        }
