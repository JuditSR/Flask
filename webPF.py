from flask import Flask, request, render_template, redirect, url_for, session
import ejercicio142
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def inici():
    return redirect(url_for('getmail'))

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
    if request.method == 'POST':
        correo = request.form['correo']
        correo = ejercicio142.BuscarUsuario(correo)
        return render_template('resultgetmail.html', correo=correo)
    else:
        return render_template('formgetmail.html')

@app.route('/addmail', methods=['POST', 'GET'])
def addmail():
    if request.method == 'POST':
        correo = request.form["correo"]
        ejercicio142.Añadir(correo)
        return render_template('resultaddmail.html', correo=correo, result_msg="Correo añadido correctamente")
    else:
        return render_template('formaddmail.html')

@app.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'POST':
        session['email'] = request.form['email_address']
        return redirect(url_for('get_email'))

@app.route('/get_email')
def get_email():
    return render_template_string("""
            {% if session['email'] %}
                <h1>Bienvenido  {{ session['email'] }}!</h1>
            {% else %}
                <h1>Bienvenido Porfavor introduce tu correo <a href="{{ url_for('set_email') }}">aquí</a></h1>
            {% endif %}
        """)

@app.route('/delete_email')
def delete_email():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    return '<h1>Session deleted!</h1>'

if __name__ == '__main__':
    app.run()