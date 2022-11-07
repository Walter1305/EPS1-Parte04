import sqlite3

def agregarProducto(codigo, nombre, precio):
    conexion = sqlite3.connect("FernandezSotelo_Almacen.db")

    lista_productos = []

    lista_productos.append(codigo)
    lista_productos.append(nombre)
    lista_productos.append(precio)

    consulta = """INSERT INTO 
               PRODUCTO(CODIGO, NOMBRE, PRECIO) 
               VALUES(?, ?, ?)
               """
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, lista_productos)
        conexion.commit()
        print("PRODUCTO AGREGADO CON ÉXITO")
    except sqlite3.OperationalError:
        print("ERROR AL INTENTAR AGREGAR EL PRODUCTO")

    conexion.close()
