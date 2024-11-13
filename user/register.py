from pymongo import MongoClient
from os import getenv
from json import dump
def register_user(doc: dict):
    """Guarda en MongoDB el formulario simplificado

    Args:
        doc (dict): Respuesta de la API de Google Forms

    Returns:
        InsertOneResponse: Respuesta obtenida de la API de MongoDB al insertar un registro
    """
    # with open('user_example.json','w') as f:
    #     dump(doc,f)
    with MongoClient(getenv('MONGO_URI')) as mongo:
        res = mongo.test.user.insert_one(doc)
    return res