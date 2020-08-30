$(document).ready(function() {
     $("#tabla").DataTable();
});

function modificar(ide) {
     window.location.href = "/modificar/" + ide;
}

function borrar(ide) {
     window.location.href = "/exec_eliminar/" + ide;
};
