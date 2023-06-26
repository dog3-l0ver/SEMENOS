import sqlite3
from sqlite3 import Error
from sql_queries import *


def connect(db):
    """connect to the database
    :param db: db file path
    :return conn: connection object"""
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, query):
    """create table
    :param conn: connection object
    :param query: sql query that creates table
    :return:"""
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)


class DataBase:
    def __init__(self):
        self.total_puffs = 0
        self.total_time = 0
        self.id = 1
        self.queries = Queries
        self.conn = connect(':memory:')
        if self.conn is not None:
            create_table(self.conn, self.queries.CurrentPuffTableCreator)
            cursor = self.conn.cursor()
            self.conn.commit()
            cursor.close()

    def close_connection(self):
        self.conn.close()

    def set_latest_current_puff(self):
        """set latest index for current_puff
        :param:
        :return:"""
        c = self.conn.cursor()
        c.execute("SELECT MAX(id) from current_puff")
        max_id = c.fetchone()
        c.close()
        return max_id[0]

    def insert_current_puff(self, query):
        """insert data related to current puff
        :param query: tuple containing all data related to current puff and device settings
        :return:"""
        c = self.conn.cursor()
        sql = ''' INSERT INTO current_puff(id, date, voltage, current, temperature, puff_length) VALUES(?,?,?,?,?,?) '''
        c.execute(sql, query)
        self.conn.commit()
        c.close()

    def select_latest_puff(self):
        """return data related to the latest puff, IT MUST BE CALLED BEFORE SELECT_PUFF_BY_ID
        :param:
        :return query: list containing all data related to the latest puff"""
        c = self.conn.cursor()
        latest = self.set_latest_current_puff()
        c.execute("SELECT * FROM current_puff WHERE id=?", (latest,))
        query = c.fetchone()
        c.close()
        return query

    def select_puff_by_id(self, ident):
        """return data related to the puff chosen by the user
        :param ident: used as a flag to prevent the user from inserting index that's out of bounds
        :return query: list containing all data related to the puff chosen by the user"""
        c = self.conn.cursor()
        c.execute("SELECT * FROM current_puff WHERE id=?", (ident,))
        query = c.fetchone()
        c.close()
        return query
