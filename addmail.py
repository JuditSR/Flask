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


@app.route('/addmail',methods = ['POST', 'GET'])
def crear():
   if request.method == 'POST':
      user = request.form['nm']
      correo = request.form['correo']
      return render_template('resultadoaddmail.html',nombre = user, correo = correo)
   else:
      return render_template('formularioaddmail.html')

if __name__ == '__main__':
   app.run(debug = True)
