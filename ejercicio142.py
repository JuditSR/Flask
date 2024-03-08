import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datosdb"
)

def BuscarUsuario(correo, contrasena):
    mycursor = mydb.cursor()
    buscar = "SELECT correo, contrasena FROM datos WHERE correo = %s"
    mycursor.execute(buscar, (correo,))
    myresult = mycursor.fetchone()

    if myresult and len(myresult) == 2 and myresult[1] == contrasena:
        return myresult[0]  # Retorna el correo encontrado
    else:
        return None


def Añadir(nombre, correo, contrasena):
    mycursor = mydb.cursor()
    sql = "INSERT INTO datos (Nombre, Correo, Contrasena) VALUES (%s, %s, %s)"
    val = (nombre, correo, contrasena,)
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
