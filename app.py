from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista en memoria para almacenar usuarios
usuarios = []

@app.route("/", methods=["GET"])
def home():
    return "<h1> Página principal</h1>"

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'informacion': 'Admin',
        'Estatus': 'Disponible'
        
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.json

    nombre = data.get('nombre')
    correo = data.get('correo')
    
   # Validar que se proporcionen ambos datos
    if not nombre or not correo:
        return jsonify({
            'Tienes un ERROR': 'Es debido tener ambos datos: nombre y correo'
        }), 400
        
    
    # Verificar si el correo ya existe creando un nuevo usuario si es otra info con un id diferente
    nuevo_usuario = {
        'nombre': nombre,
        'correo': correo,
        'id': len(usuarios) + 1
        
        
    }
    
    # Agregar el nuevo usuario a la lista de usuarios
    usuarios.append(nuevo_usuario)
    
    return jsonify({
    "mensaje": "Usuario creado exitosamente!",
    " Informacion del usuario": nuevo_usuario }), 201
    
    

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)



if __name__ == '__main__':
    app.run(debug=True)
