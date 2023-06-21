import sqlite3
from sqlite3 import Error
from sql_queries import *


def connect(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)


class DataBase:
    def __init__(self):
        self.queries = Queries
        self.conn = connect(r".\db\database.db")
        if self.conn is not None:
            create_table(self.conn, self.queries.BatteryTableCreator)
            create_table(self.conn, self.queries.CoilTableCreator)
            create_table(self.conn, self.queries.PuffTableCreator)
