$(function () {
     $("#btnModificar").click(function (e) {
          e.preventDefault();
          $.ajax({
               url: "/exec_modificar",
               data: $("form").serialize(),
               type: "POST",
               success: function (response) {
                    if (response == 'exito') {
                         // console.log(response);
                         window.location.href = "/";
                         $("#mensaje").innnerHTML = 'Datos Actualizados';
                         $("#alerta").removeClass("hide");
                         
                    }
               },
               error: function (error) {
                    console.log(error);
               },
          });
     });
});

