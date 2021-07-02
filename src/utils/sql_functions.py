import sqlalchemy
import mysql.connector

def mysql_connect():
    ''' Allow the connection to the mysql database coach_diary '''
    from conf.conf_connect import mysql_pseudo, mysql_pw
    mysql_username = mysql_pseudo
    mysql_password = mysql_pw
    database_name = 'coach_diary'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_username, mysql_password, database_name), pool_recycle=1, pool_timeout=57600).connect()
    return database_connection


# Creation of the tables
def create_client_table(db_connection):
    ''' Create the client table'''
    query = ''' CREATE TABLE IF NOT EXISTS client(
    id_client INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    firstname VARCHAR(30),
    information VARCHAR(250),
    PRIMARY KEY (id_customer)
    )'''
    db_connection.execute(query)

def create_text_table(db_connection):
    """ Create the text table """
    query = '''CREATE TABLE IF NOT EXISTS text(
        id_text INT NOT NULL,
        content TEXT NOT NULL,
        creation_date DATE NOT NULL,
        modification_date DATE,
        id_client INT NOT NULL,
        PRIMARY KEY (id_text),
        FOREIGN KEY (id_client) REFERENCES client(id_client)  
        )'''
    db_connection.execute(query)

# Testing query
def test_add_client(db_connection):
    query = """INSERT INTO client (id_client, name, firstname, information)
        VALUES (0, Doe, John, new client
        )"""
    db_connection.execute(query)