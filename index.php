{% extends "templates/layout.php"%}

{% block titulo %}
<script>
     $(document).ready(function() {
          $('#tabla').DataTable();
     });

     function modificar(ide) {
          window.location.href = "/modificar/" + ide;
     }

     function borrar(ide) {
          window.location.href = "/exec_eliminar/" + ide;
     }
</script>
<title>Hecho con Flask</title>
{% endblock %}

{% block contenido %}
{% with messages = get_flashed_messages()  %}
{% if messages %}
{% for message in messages %}
<div style="background-color: #A3CB38;" class="text-white mt-2 alert alert-dismissible fade show" role="alert">
     <strong>{{ message }}</strong>
     <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
     </button>
</div>
{% endfor %}
{% endif %}
{% endwith %}


<div class="card card-header">
     <div style="background-color: #006266;" class="mb-3 ">
          <div class="form-row m-2 text-center align-items-center">
               <div class="col-md-10">
                    <h3 class="text-white float-left text-uppercase">Control de datos con Flask</h3>
               </div>
               <div class="col-md-2">
                    <a style="background-color: #1B1464;" class="h-100 border-0 btn btn-primary btn-sm p-2" href="{{ url_for('agregar') }}">Nuevo Dato</a>
               </div>
          </div>
     </div>
     <table id="tabla" class=" table table-sm">
          <thead class="thead-dark">
               <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Título</th>
                    <th scope="col">Descripción</th>
                    <th scope="col">Controles</th>
               </tr>
          </thead>
          <tbody>
               {% for dato in datos %}
               <tr>
                    <th scope="row">{{ dato.ID}}</th>
                    <td>{{ dato.Texto}}</td>
                    <td>{{ dato.Descripcion}}</td>
                    <td>
                         <button class="btn btn-success btn-sm" onclick="modificar({{ dato.ID }});">Editar</button>
                         <button class="btn btn-danger btn-sm" onclick="borrar({{ dato.ID }});">Borrar</button>
                    </td>
               </tr>
               {% endfor %}
          </tbody>
     </table>
</div>
{% endblock %}