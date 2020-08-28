#import pyodbc
import psycopg2
#import pg
from data.clsDatos import clsDatos

class clsConexion():
     # Declara las variables para la conexion con PostgreSQL
     _servidor = 'localhost' # Estoy utilizando Docker
     _basedatos = 'DatosPython'
     _usuario = 'postgres'
     _contra = 'Vsmora1989'
     
     # Declara las variables para la conexion con SQL Server
     # _servidor = 'localhost,1433' # Estoy utilizando Docker
     # _basedatos = 'datos'
     # _usuario = 'jperez'
     # _contra = 'Vsmora1989'

     def __init__(self):
          pass

     def _conectar(self):
          try:
               #Conexion con PostgreSQL
               _conex = psycopg2.connect(host=self._servidor, database=self._basedatos, user=self._usuario, password=self._contra)
               print(_conex)
               #print('exito conex')
               #Conexion con Sql Server
               # _conex = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
               #                     'SERVER=' + self._servidor +
               #                     ';DATABASE=' + self._basedatos +
               #                     ';UID=' + self._usuario +
               #                     ';PWD=' + self._contra)
          except Exception as err:
               print(err)
          return _conex

     def agregar(self, dato):
          estado = False
          AuxSql = "insert into datos(texto, descripcion) values('{0}','{1}')".format(dato.Texto, dato.Descripcion)
          try:
               _conex = self._conectar()
               with _conex.cursor() as cursor:
                    cursor.execute(AuxSql)

               _conex.close()
               estado = True
          except Exception as err:
               print(err)
          return estado

     def editar(self, dato):
          estado = False
          AuxSql = "update datos set texto = '{1}', descripcion = '{2}' where id = {0}".format(dato.ID, dato.Texto, dato.Descripcion)
          try:
               _conex = self._conectar()
               with _conex.cursor() as cursor:
                    cursor.execute(AuxSql)

               _conex.close()
               estado = True
          except Exception as err:
               print(err)
          return estado

     def borrar(self, ide):
          estado = False
          AuxSql = "delete datos where id = {0}".format(ide)
          try:
               _conex = self._conectar()
               with _conex.cursor() as cursor:
                    cursor.execute(AuxSql)

               _conex.close()
               estado = True
          except Exception as err:
               print(err)
          return estado

     def consultar(self, ide=None):
          data = ''
          salida = []

          try:
               _conex = self._conectar()
               with _conex.cursor() as cursor:
                    if ide == None:
                         cursor.execute("Select * from datos")
                    else:
                         cursor.execute("Select * from datos where id = {0}".format(ide))
                         
                    data = cursor.fetchall()
                    _conex.close()
          except Exception as err:
               print(err)

          for tupla in data:
               salida.append(clsDatos(tupla[0], tupla[1], tupla[2]))

          return salida
