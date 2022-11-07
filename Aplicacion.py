import sqlite3
def iniciarBD():
    conexion = sqlite3.connect("FernandezSotelo_Almacen.db")

    tabla_producto = """CREATE TABLE PRODUCTO(
                     IDPRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
                     CODIGO TEXT UNIQUE,
                     NOMBRE TEXT,
                     PRECIO REAL
                     )"""

    try:
        cursor = conexion.cursor()
        cursor.execute(tabla_producto)
    except sqlite3.OperationalError:
        pass

def menu():
    iniciarBD()

    print("\t\t\t\t\t**MENÚ DE OPCIONES**")
    print("1. Registrar\n" +
          "2. Eliminar\n" +
          "3. Editar\n" +
          "4. Listar\n" +
          "5. Salir\n")
    opcionMenu = int(input("Digite la opción: "))

    if(opcionMenu == 1):
        import Registrar
        
    elif(opcionMenu == 2):
        import Eliminar
    elif(opcionMenu == 3):
        import Editar
    elif(opcionMenu == 4):
        import Listar
    elif(opcionMenu == 5):
        print("PROGRAMA FINALIZADO CON ÉXITO")
        exit()

menu()