'''
import pymysql
import pymysql.cursors
import creds
import boto3

# # ----------------
# # Section 1: MySQL (RDS) Connection Helpers
# # ----------------

# def get_conn():
#     """
#     Established and return a connection to the MySQL RDS database
#     using credentials from creds.py
#     Uses DictCursor to return query results as dictionaries.
#     """
def get_conn():
    """
    Establish and return a connection to the MySQL RDS database
    using credentials from creds.py
    Uses DictCursor to return query results as dictionari
    """
    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )



def execute_query(query, args=()):
    """
    Execute a SQL query using a connection to RDS.
    Closes the connectio automatically after running the query
    Returns the results as a list of dictionaries.
    """
    conn = get_conn()
    try: 
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows 
    finally:
        conn.close()


def get_list_of_dictionaries():
    """
    Returns the top 10 countries from the 'country' table, 
    including name and population. Use on the homepage. 
    """
    query = "SELECT Name, Population FROM country Limit 10;"
    return execute_query(query)
'''


import pymysql
import pymysql.cursors
import creds
import boto3

# # ----------------
# # Section 1: MySQL (RDS) Connection Helpers
# # ----------------

# def get_conn():
#     """
#     Established and return a connection to the MySQL RDS database
#     using credentials from creds.py
#     Uses DictCursor to return query results as dictionaries.
#     """
def get_conn():
    """
    Establish and return a connection to the MySQL RDS database
    using credentials from creds.py
    Uses DictCursor to return query results as dictionari
    """
    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )



def execute_query(query, args=()):
    """
    Execute a SQL query using a connection to RDS.
    Closes the connectio automatically after running the query
    Returns the results as a list of dictionaries.
    """
    conn = get_conn()
    try: 
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows 
    finally:
        conn.close()


def get_list_of_dictionaries():
    """
    Returns the top 10 countries from the 'country' table, 
    including name and population. Use on the homepage. 
    """
    query = "SELECT Name, Population FROM country Limit 10;"
    return execute_query(query)

# def get_languages():



#     try:
#         with conn.cursor() as cur:
#             cur.execute(query, args)
#             row = cur.fetchall()
#         return rows
#     finally:
#         conn.close()


# def get_lists_of_dictionaries():
#     """
#     """
#     query = "SELECT Name, Population FROM country LIMIT 10;