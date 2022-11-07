import sqlite3

def listarProductos():

    conexion = sqlite3.connect("FernandezSotelo_Almacen.db")

    consulta = """ SELECT * FROM PRODUCTO
               """

    cursor = conexion.cursor()
    cursor.execute(consulta)
    productos = cursor.fetchall()

    fila_productos = []

    for producto in productos:
        fila_productos.append(producto[1])
        fila_productos.append(producto[2])
        fila_productos.append(producto[3])

    conexion.close()
