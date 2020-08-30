{% extends "layout.php"%}

{% block titulo %}
<script src="{{url_for("static", filename="js/jquery-3.5.1.js")}}"></script>
<script src="{{url_for("static", filename="js/agregarRegistro.js")}}"></script>

<title>Agregar datos con Flask</title>
{% endblock %}

{% block contenido %}

<div class="container w-50 mt-3">
     <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12">
               <div class="card">
                    <div class="card-header text-center text-uppercase">
                         <h3>Agregando nuevo registro con Flask</h3>
                    </div>
                    <div class="card-body">
                         <form class="form" action="{{url_for("agregar")}}" method="POST">
                              <div class="from-group row mb-1">
                                   <label for="txtTexto" class="col-sm-3 col-form-label"><strong>Texto</strong></label>
                                   <div class="col-sm-9">
                                        <input type="text" id="txtTexto" name="txtTexto" class="form-control" required>
                                   </div>
                              </div>
                              <div class="from-group row">
                                   <label for="txtDescrip" class="col-sm-3 col-form-label"><strong>Descripción</strong></label>
                                   <div class="col-sm-9">
                                        <input type="text" id="txtDescrip" name="txtDescrip" class="form-control" required>
                                   </div>
                              </div>
                    </div>
                    <div class="card-footer">
                         <button style="background-color: #1B1464;" type="submit" class="btn text-white btn-block">
                              <h4>Agregar</h4>
                         </button>
                    </div>
                    </form>
               </div>
          </div>
     </div>
</div>

{% endblock %}