$(function () {
     $("#btnAgregar").click(function (e) {
          e.preventDefault();
          $.ajax({
               url: "/agregar",
               data: $("form").serialize(),
               type: "POST",
               success: function (response) {
                    console.log(response);
                    window.location.href = "/";
                    $("#mensaje").innnerHTML = response;
                    $("#alerta").removeClass("hide");
               },
               error: function (error) {
                    console.log(error);
               },
          });
     });
});
