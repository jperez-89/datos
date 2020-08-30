<body class="container-fluid">
     <header class="col-md-12">
          <nav style="background-color: #006266;" class="navbar navbar-expand-lg text-uppercase ">
               <a class="navbar-brand text-white" href="/">Datos</a>
               <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
               </button>

               <div class="collapse navbar-collapse " id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                         <!-- <li class="nav-item active">
                              <a class="nav-link" href="/">Inicio</a>
                         </li> -->
                         <!-- <li class="nav-item ">
                              <a class="nav-link text-white" href="#">Página 1</a>
                         </li> -->
                    </ul>
               </div>
          </nav>
     </header>
     <main class="">
          <div class="container-fluid">
               {% block contenido %}
               {% endblock %}
          </div>
     </main>

     <footer class="col-md-12"></footer>
</body>

</html>