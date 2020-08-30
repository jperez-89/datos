import psycopg2
from data.clsDatos import clsDatos

class clsConexion():
     # Declara las variables para la conexion con PostgreSQL
     _servidor = 'ec2-107-20-15-85.compute-1.amazonaws.com'
     _basedatos = 'd6ju6p7ghvss0v'
     _usuario = 'mgooiwdzbwjgav'
     _contra = '24bd3d042f755e73b4c5daf58ef1008ca4d0731c12ab89a28fd9e133abd03d67'
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
