import sqlite3
from datetime import date


def set_sql_connection(file):
    """
    This function will create connection to a database, using sqlite3 module
    This function returns a Connection object 
    """
    con = sqlite3.connect(file)
    return con


def set_cursor(con):
    """
    This function will create a Cursor object, once a connection had been made using set_sql_connection
    IN: con
    TYPE: sqlite3.connect
    OUT: cur
    TYPE: sqlite3.connect.cursor
    """
    cur = con.cursor()
    return cur


def close_sql_connection(con):
    """
    This function will commit any changes to an open sql connection and closes it.
    IN: con
    TYPE: sqlite3.connect 
    """
    con.commit()
    con.close()


def get_items():
    """
    This function retrieves all users information from a database
    IN: 
    OUT: Values from DB as LIST of Dict
    Type: LIST
    """
    con = set_sql_connection()  # Creates connection
    cur = set_cursor(con)  # Creates Cursor
    query = "SELECT * FROM Inventory"  # SQL QUERY
    data = cur.execute(query).fetchall()  # EXECUTING SQL QUERY
    dct = sort_as_dict(cur, data)
    close_sql_connection(con)  # Closing connection
    return dct


def sort_as_dict(cur, data):
    """
    This function receives cur, data, where:
    1. cur will be used to retrieve columns
    2. data will be used to retrieve values
    This function will return a list of dictionary {columns:values}
    """
    # List Comprehension
    # GETTING COLUMNS NAMES FROM DB
    columns = [desc[0] for desc in cur.description]
    result = []
    for row in data:
        row = dict(zip(columns, row))
        result.append(row)

    return result
