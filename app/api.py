from flask import jsonify, Blueprint, request
from app import querys as q
from app.models import Usuario

api = Blueprint('api',__name__,url_prefix='/api/v1')

@api.route('/')
def index():
    return jsonify({'status': 'ok'}), 200

@api.route('/usuario', methods=['GET'])
def get():
    usuarios = q.get()
    return jsonify(usuarios), 200

@api.route('/usuario/<int:id>', methods=['GET'])
def getId(id):
    usuario = q.get(id)

    return jsonify(usuario), 200

@api.route('/usuario', methods=['POST'])
def post():
    response = request.get_json()

    name = response['name']
    age = response['age']
    height = response['height']

    usuario = Usuario(name,age,height)
    q.post(usuario)

    return jsonify({name : 'Created'}), 201


@api.route('/usuario/<int:id>', methods=['PUT'])
def put(id):
    response = request.get_json()

    name = response['name']
    age = response['age']
    height = response['height']

    usuario = Usuario(name,age,height)
    user = q.get(id)
    if user:
        q.put(id,usuario)
        return jsonify({user['name'] : 'Updated'}), 200
    else:   
        return jsonify({'Error': 'User not found'}), 404


@api.route('/usuario/<int:id>', methods=['DELETE'])
def delete(id):
    usuario = q.get(id)
    if(usuario):
        q.delete(id)
        return jsonify({usuario['name'] : 'deleted'}), 200
    else:
        return jsonify({'Error' : 'User not Found'}), 404