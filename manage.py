from data.clsDatos import clsDatos
# from data.clsConexion import clsConexion
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)

# settings
# app.secret_key = "mysecretkey"

# Se agrega una instancia de la clase
# conex = clsConexion()



# class clsConexion():
     # Declara las variables para la conexion con PostgreSQL
_servidor = 'ec2-34-233-131-94.compute-1.amazonaws.com'
_basedatos = 'd67lgai574pj75'
_usuario = 'uhoewfjxxtumic'
_contra = '10a98148795ac97b6e98f97be49e1308126e698cdf8f6a87395cebc903a929c8'
_puerto = '5432'
     
     # _servidor = 'localhost'
     # _basedatos = 'DatosPython'
     # _usuario = 'postgres'
     # _contra = 'Vsmora1989'
     # _puerto = '5432'
     
     # postgres://mgooiwdzbwjgav:24bd3d042f755e73b4c5daf58ef1008ca4d0731c12ab89a28fd9e133abd03d67@ec2-107-20-15-85.compute-1.amazonaws.com:5432/d6ju6p7ghvss0v

def _conectar(self):
     try:
          #Conexion con PostgreSQL
          _conex = psycopg2.connect(user=self._usuario,
                                        password=self._contra,
                                        host=self._servidor,
                                        port=self._puerto,
                                        database=self._basedatos)
     except Exception as err:
          print(err)

     return _conex

# METODO DE AGREGAR <-----------------------------
def agregar(self, dato):
     estado = False
     AuxSql = "INSERT INTO datos(texto, descripcion) VALUES('{0}','{1}');".format(dato.Texto, dato.Descripcion)
     try:
          _conex = self._conectar()
          with _conex.cursor() as cursor:
               cursor.execute(AuxSql)
               _conex.commit()
               estado = True
          _conex.close()
     except Exception as err:
          print(err)

     # finally:
     #      cursor.close()
     #      _conex.close()

     return estado

# METODO DE EDITAR <-----------------------------
def editar(self, dato):
     estado = False
     AuxSql = "UPDATE datos SET texto = '{1}', descripcion = '{2}' WHERE id = {0}".format(dato.ID, dato.Texto, dato.Descripcion)
     try:
          _conex = self._conectar()
          with _conex.cursor() as cursor:
               cursor.execute(AuxSql)
               _conex.commit()
               estado = True
          _conex.close()

     except Exception as err:
          print(err)

     # finally:
     #      cursor.close()
     #      _conex.close()

     return estado

     # METODO DE BORRAR <-----------------------------
def borrar(self, ide):
     estado = False
     AuxSql = "DELETE FROM datos WHERE id = {0}".format(ide)
     try:
          _conex = self._conectar()
          with _conex.cursor() as cursor:
               cursor.execute(AuxSql)
               _conex.commit()
               estado = True
          _conex.close()

     except Exception as err:
          print(err)

     # finally:
     #      cursor.close()
     #      _conex.close()

     return estado

# METODO DE CONSULTAR <-----------------------------
def consultar(self, ide=None):
     data = ''
     salida = []
     try:
          _conex = self._conectar()
          with _conex.cursor() as cursor:
               if ide == None:
                    cursor.execute("SELECT * FROM datos")
               else:
                    cursor.execute("SELECT * FROM datos WHERE id = {0}".format(ide))

               data = cursor.fetchall()
          _conex.close()

     except Exception as err:
          print(err)

     # finally:
          # cursor.close()
          # _conex.close()

     for tupla in data:
          salida.append(clsDatos(tupla[0], tupla[1], tupla[2]))

     return salida
     
     

# Ruta principal, retorna los datos que existen en la base de datos
@app.route('/')
def index():
     return render_template('index.html', datos=consultar())

# Ruta de agregar datos a la db.
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
     if request.method == "POST":
          # Ejecuta el metodo agregar de la clase ClsConexion
          if agregar(clsDatos(0, request.form['txtTexto'], request.form['txtDescrip'])):
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
     return render_template('modificar.html', datos=consultar(ide))

# Ruta modificar con POST.
@app.route('/exec_modificar', methods=['POST'])
def exec_modificar():
     # Ejecuta el metodo editar de la clase ClsConexion para actualizar los datos
     if editar(clsDatos(request.form['txtID'], request.form['txtTexto'], request.form['txtDescrip'])):
          flash('Datos actualizados correctamente')
     else:
          flash('Se presentó un problema con los datos')
     # Al finalizar retorna la index
     return redirect(url_for('index'))

# Ruta eliminar
@app.route('/exec_eliminar/<int:ide>', methods=['GET'])
def exec_eliminar(ide):
     # Ejecuta el metodo borrar de la clase ClsConexion
     if borrar(ide):
          flash('Datos eliminados correctamente')
     else:
          flash('Se presentó un problema con los datos')
     # Al finalizar retorna la index
     return redirect(url_for('index'))


if __name__ == '__main__': 
     app.run(debug=True)
