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
        self.latest = 1
        self.id = 1
        self.queries = Queries
        self.conn = connect(':memory:')
        if self.conn is not None:
            create_table(self.conn, self.queries.CurrentPuffTableCreator)
            create_table(self.conn, self.queries.PuffsTableCreator)

    def insert_current_puff(self, query):
        """insert data related to current puff
        :param query: tuple containing all data related to current puff and device settings
        :return:"""
        c = self.conn.cursor()
        sql = ''' INSERT INTO current_puff(id, date, voltage, current, temperature, puff_length) VALUES(?,?,?,?,?,?) '''
        c.execute(sql, query)
        self.conn.commit()
        c.close()

    def update_puffs(self, time):
        """update data related to information about all puffs
        :param time: length of current puff, floating point number
        :return:"""
        c = self.conn.cursor()
        c.execute("SELECT time_sum, puff_count FROM puffs WHERE id=?", (self.id, ))
        data = c.fetchone()
        actual_time = data[0] + time
        actual_puff_count = data[1] + 1
        sql = '''INSERT INTO puffs(id, time_sum, puff_count) VALUES(?,?,?)'''
        c.execute(sql, (self.id, actual_time, actual_puff_count))
        self.conn.commit()
        c.close()
        self.id += 1

    def select_latest_puff(self):
        """return data related to the latest puff, IT MUST BE CALLED BEFORE SELECT_PUFF_BY_ID
        :param:
        :return query: list containing all data related to the latest puff"""
        c = self.conn.cursor()
        self.latest = c.lastrowid
        c.execute("SELECT * FROM current_puff WHERE id=?", (self.latest,))
        query = c.fetchone()
        c.close()
        return query

    def select_puff_by_id(self, ident):
        """return data related to the puff chosen by the user
        :param ident: used as a flag to prevent the user from inserting index that's out of bounds
        :return query: list containing all data related to the puff chosen by the user"""
        c = self.conn.cursor()
        if ident <= self.latest:
            c.execute("SELECT * FROM current_puff WHERE id=?", (ident,))
        else:
            c.execute("SELECT * FROM current_puff WHERE id=?", (self.latest, ))
        query = c.fetchone()
        c.close()
        return query

    def select_puffs(self):
        """return data related to information about all puffs
        :param:
        :return query: list containing data related to information about all puffs"""
        c = self.conn.cursor()
        last = c.lastrowid
        c.execute("SELECT * FROM puffs WHERE id=?", (last,))
        query = c.fetchone()
        c.close()
        return query
