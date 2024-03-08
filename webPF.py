from flask import Flask, request, render_template, redirect, url_for, session
import ejercicio142
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def inici():
    return redirect(url_for('publica'))

@app.route('/publica')
def publica():
        return render_template('paginasinlogin.html')

@app.route('/getmail', methods=['POST', 'GET'])
def getmail():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = ejercicio142.BuscarUsuario(correo, contrasena)

        if usuario:
            session['email'] = correo
            return redirect(url_for('webpf'))
        else:
            error_message = "Credenciales incorrectas"
            return render_template('iniciarsesionresult.html', correo=correo, error_message=error_message)
    else:
        return render_template('iniciarsesionPF.html')



@app.route('/addmail', methods=['POST', 'GET'])
def addmail():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]
        ejercicio142.Añadir(nombre, correo, contrasena)
        return render_template('resultadoanadirusuarioPF.html', correo=correo, result_msg="Correo añadido correctamente")
    else:
        return render_template('crearusuarioPF.html')

@app.route('/delete_email')
def delete_email():
    session.pop('email', default=None)
    return redirect(url_for('publica'))

if __name__ == '__main__':
    app.run()

@app.route('/webpf')
def webpf():
    if 'email' in session:
        return render_template('webpf.html', email=session['email'])
    else:
        return redirect(url_for('getmail'))

@app.route('/formulario')
def formulario():
        return render_template('formularioPF2.html')


@app.route('/aboutme')
def aboutme():
        return render_template('aboutmePF.html')