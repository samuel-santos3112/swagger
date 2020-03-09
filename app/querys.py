from app.models import Usuario
from app.connection import Session

from sqlalchemy import desc


def internal_error(error, session=None):
    mensagem = {
        'status': 500,
        'message_user': 'Erro Interno do Servidor',
        'message_dev': str(error),
    }


def get(id=None):
    try:
        session = Session()
        if id:
            user = session.query(Usuario).filter(Usuario.id == id).first()
            usuario = user.to_dict()
            return usuario
        else:
            users = session.query(Usuario).all()
            usr = []
            for user in users:
                dic_usr = {
                    'id' : user.id,
                    'name' : user.name,
                    'age' : user.age,
                    'height' : str(user.height)
                }
                usr.append(dic_usr)
            return usr

    except Exception as e:
        return internal_error(e), 500

    finally:
        session.close()

def post(usuario):
    try:
        session = Session()
        session.add(usuario)
        session.commit()
        session.refresh()
    except Exception as e:
        return internal_error(e), 500
    finally:
        session.close()

def put(id, usuario):
    try:
        session = Session()
        session.query(Usuario).filter(Usuario.id==id).update({
            Usuario.name : usuario.name,
            Usuario.age : usuario.age,
            Usuario.height : usuario.height
        })
        session.commit()
    except Exception as e:
        return internal_error(e), 500
    finally:
        session.close()

def delete(id):
    try:
        session = Session()
        usuario = session.query(Usuario).filter(Usuario.id==id).first()
        if usuario:
            session.delete(usuario)
            session.commit()
        else:
            return jsonify({'Error' : 'User not Found'}), 404
    except Exception as e:
        return internal_error(e), 500
    finally:
        session.close()
