import mysql.connector

#Acceder al localhost y crear la base de datos.
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#)
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE datosdb")

#Comprobar que existe la base de datos
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)

#Conectarse a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datosdb"
)

#Crear tabla
#mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE Datos (Nombre VARCHAR(255), Correo VARCHAR(255))")

#Crear clave primaria
#mycursor = mydb.cursor()
#mycursor.execute("ALTER TABLE datos ADD PRIMARY KEY (Nombre)")

#Insertar los datos
#mycursor = mydb.cursor()
#sql = "INSERT INTO datos (Nombre, Correo) VALUES (%s, %s)"
#val = [
#  ('Mercedes','mcast386@xtec.cat'),
#  ('Rayane','rayane@rayane.sa'),
#  ('Mohamed','moha@gmail.com'),
#  ('Jad','jad@gmail.com'),
#  ('Oriol','joam@gmail.com'),
#  ('Elias','hola123@gmail.com'),
#  ('Armau','arnau@gmail.com'),
#  ('Asdrubal','asdrubal@gmail.com'),
#  ('Adrian','pedrosanchez@asix2.com'),
#  ('Eric','eric@gmail.com'),
#  ('Emma','pacosanz@gmail.com'),
#  ('nishwan','nishwan@gmail.com'),
#  ('Javi','javi@gmail.com'),
#  ('Novel','novelferreras49@gmail.com'),
#  ('Bruno','elcigala@gmail.com'),
#  ('David','argentino@gmail.com'),
#  ('Judit','judit@gmail.com'),
#  ('Joao','joao@gmail.com'),
#  ('Laura','laura@gmail.com'),
#  ('enrico','123@gmail.com'),
#  ('Joel','joelcobre@gmail.com'),
#  ('Aaron','aaron@gmail.com'),
#  ('Moad','moad@gmail.com')
#]
#mycursor.executemany(sql, val)
#mydb.commit()
#print(mycursor.rowcount, "filas insertadas")

def BuscarUsuario(nombrebuscar): 
    mycursor = mydb.cursor()
    #nombrebuscar = input ("Introduce un nombre para buscar su correo electrónico: ")
    buscar = "SELECT Correo FROM datos WHERE Nombre = '" + nombrebuscar + "'" 
    mycursor.execute(buscar)
    myresult = mycursor.fetchall()
    if myresult is not None:
        return myresult[0]  # Retorna el correo encontrado
    else:
        return "NOTROBAT"

def Añadir(nombre,correo):
#Añadir usuario y correo
    #nombre = input("Introduce tu nombre: ")
    #correo = input("Introduce tu correo: ")
    mycursor = mydb.cursor()
    sql = "INSERT INTO datos (Nombre, Correo) VALUES (%s, %s)"
    val = (nombre, correo)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Fila insertada correctamente")

#Ver datos de la tabla
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
