# library_manage
import pymysql
from pymysql.cursors import DictCursor

class DB(object):
    """Initialize mysql database """
    host = "localhost"
    user = "root"
    password = ""
    db = "lms"
    table = ""

    def __init__(self, app):
        # Establish a persistent connection pool connection using PyMySQL directly
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db,
            cursorclass=DictCursor,
            autocommit=True # Keeps transactions handling smoothly
        )
        
        # --- ADDED: Turn off Strict Mode right on startup ---
        with self.connection.cursor() as cursor:
            cursor.execute("SET SESSION sql_mode='';")

    def cur(self):
        # Ensures the connection is still open and returns a fresh cursor
        self.connection.ping(reconnect=True)
        
        # --- ADDED: Keep Strict Mode turned off if it reconnects ---
        cursor = self.connection.cursor()
        cursor.execute("SET SESSION sql_mode='';")
        return cursor

    def query(self, q):
        h = self.cur()
    
        if (len(self.table) > 0):
            q = q.replace("@table", self.table)

        h.execute(q)
        return h

    def commit(self):
        self.connection.commit()