import mysql.connector

__cnx=None

def getSQLConnection():
    print("establishing a SQL connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root',
                                      host='127.0.0.1',
                                      database='grocerystore')

    return __cnx











