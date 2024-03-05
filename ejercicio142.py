import mysql.connector

#Conectarse a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datosdb"
)

def BuscarUsuario(correo_buscar): 
    mycursor = mydb.cursor()
    buscar = "SELECT Correo FROM datos WHERE Correo = %s"
    mycursor.execute(buscar, (correo_buscar,))
    myresult = mycursor.fetchone()
    if myresult is not None:
        return myresult[0]  # Retorna el correo encontrado
    else:
        return "NOTROBAT"


def Añadir(correo):
    mycursor = mydb.cursor()
    sql = "INSERT INTO datos (Correo) VALUES (%s)"
    val = (correo,) 
    mycursor.execute(sql, val)
    mydb.commit()
    print("Fila insertada correctamente")


def VerDatos():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM datos")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#Menu
while True:
        print("\n1. Buscar correo")
        print("2. Añadir usuario y correo")
        print("3. Ver Tabla")
        print("4. Salir")
        opcion= (int)(input("Introduce una opción: "))
        if opcion == 1:
            BuscarUsuario()
        elif opcion == 2:
            Añadir()
        elif opcion == 3:
            VerDatos()
        elif opcion == 4:
            break
        else:
            print("Introduce un número válido")
