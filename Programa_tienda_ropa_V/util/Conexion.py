import mysql.connector

def conectar_bd():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tiendaropa2",
    )
        # Crear un cursor
    cursor = conn.cursor()
    return conn, cursor
   

def close_bd():
    conn = mysql.connector.connect(
        host="localhost",
        user="seiya",
        password="12433",
        database="tienda_ropa",
    )
        # Crear un cursor
    cursor = conn.cursor()
    cursor.close()
    conn.close()