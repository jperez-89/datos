from data.clsDatos import clsDatos
from data.clsConexion import clsConexion
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

# Se agrega una instancia de la clase
conex = clsConexion()

# Ruta principal, retorna los datos que existen en la base de datos
@app.route('/')
def index():
     return render_template('index.html', datos=conex.consultar())

# Ruta de agregar datos a la db.
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
     if request.method == "POST":
          # Ejecuta el metodo agregar de la clase ClsConexion
          if conex.agregar(clsDatos(0, request.form['txtTexto'], request.form['txtDescrip'])):
               flash('Datos almacenados correctamente')
          else:
               flash('Se presentó un problema con los datos')
          # Cuando agrega retorna la index 
          return redirect(url_for("index"))
     else:
          # Cuando se llama ejecuta la vista de agregar
          return render_template('agregar.html')

# Ruta modificar con GET, trae los datos que se quieren modificar para mostrarlos en la vista modificar
@app.route('/modificar/<int:ide>', methods=['GET'])
def modificar(ide):
     return render_template('modificar.html', datos=conex.consultar(ide))

# Ruta modificar con POST.
@app.route('/exec_modificar', methods=['POST'])
def exec_modificar():
     # Ejecuta el metodo editar de la clase ClsConexion para actualizar los datos
     if conex.editar(clsDatos(request.form['txtID'], request.form['txtTexto'], request.form['txtDescrip'])):
          flash('Datos actualizados correctamente')
     else:
          flash('Se presentó un problema con los datos')
     # Al finalizar retorna la index
     return redirect(url_for('index'))

# Ruta eliminar
@app.route('/exec_eliminar/<int:ide>', methods=['GET'])
def exec_eliminar(ide):
     # Ejecuta el metodo borrar de la clase ClsConexion
     if conex.borrar(ide):
          flash('Datos eliminados correctamente')
     else:
          flash('Se presentó un problema con los datos')
     # Al finalizar retorna la index
     return redirect(url_for('index'))


if __name__ == '__main__': 
     app.run(host='0.0.0.0', port=5001, debug=True)
