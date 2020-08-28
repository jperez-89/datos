from data.clsDatos import clsDatos
from data.clsConexion import clsConexion
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

conex = clsConexion()

@app.route('/')
def index():
     return render_template('index.html', datos=conex.consultar())


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
     if request.method == "POST":
          if conex.agregar(clsDatos(0, request.form['txtTexto'], request.form['txtDescrip'])):
               flash('Datos almacenados correctamente')
          else:
               flash('Se presentó un problema con los datos')
          return redirect(url_for("index"))
     else:
          return render_template('agregar.html')


@app.route('/modificar/<int:ide>', methods=['GET'])
def modificar(ide):
     return render_template('modificar.html', datos=conex.consultar(ide))


@app.route('/exec_modificar', methods=['POST'])
def exec_modificar():
     if conex.editar(clsDatos(request.form['txtID'], request.form['txtTexto'], request.form['txtDescrip'])):
          flash('Datos actualizados correctamente')
     else:
          flash('Se presentó un problema con los datos')
     return redirect(url_for('index'))


@app.route('/exec_eliminar/<int:ide>', methods=['GET'])
def exec_eliminar(ide):
     if conex.borrar(ide):
          flash('Datos eliminados correctamente')
     else:
          flash('Se presentó un problema con los datos')
     return redirect(url_for('index'))


if __name__ == '__main__': 
     app.run(host='127.0.0.1', port=5001, debug=True)
