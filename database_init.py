# database_init.py
from Models.DAO import DAO

db_instance = None

def init_db(app):
    global db_instance
    db_instance = DAO(app)
    return db_instance