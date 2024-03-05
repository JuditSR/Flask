from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request
import sys
import csv

app = Flask(__name__)

def buscar_correo(nombreinsertar):
   with open('nomemail.csv', 'r') as diccionario:
      csv_leer = csv.reader(diccionario)
  
      for row in csv_leer:
         nombre = row[0]
         correo = row[1]
         if nombreinsertar == nombre:  
            return correo

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      user = request.form['nom']
      correo = buscar_correo(user)
      if correo:
         return render_template('resultadogetmail.html',nombre = user, correo = correo)
      else:
         return 'Usuario no encontrado'
   else:
      return render_template('formulariogetmail.html')

if __name__ == '__main__':
   app.run(debug = True)
