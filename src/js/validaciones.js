
$(document).ready(function () {

    //validation of password requirements
    $('#password-require').hide();
    $('#passwordnew').keyup(function () {
        // keyup code here
        var passwd = $(this).val();
        //letter
        if (passwd.match(/[A-z]/)) {
            $('#letter').removeClass('invalid').addClass('valid');
        } else {
            $('#letter').removeClass('valid').addClass('invalid');
        }
        //capital letter
        if (passwd.match(/[A-Z]/)) {
            $('#capital').removeClass('invalid').addClass('valid');
        } else {
            $('#capital').removeClass('valid').addClass('invalid');
        }
        //number
        if (passwd.match(/\d/)) {
            $('#number').removeClass('invalid').addClass('valid');
        } else {
            $('#number').removeClass('valid').addClass('invalid');
        }
        //length
        if (passwd.length < 8) {
            $('#length').removeClass('valid').addClass('invalid');
        } else {
            $('#length').removeClass('invalid').addClass('valid');
        }
        //special characters
        // if (passwd.match(/^\s*[~!@#$%^&*\s]+\s*$/)){
        //   $('#character').removeClass('valid').addClass('invalid');
        // } else {
        //   $('#character').removeClass('invalid').addClass('valid');
        // }


    }).focus(function () {
        $('#password-require').show();
    }).blur(function () {
        $('#password-require').hide();
    });

    //matching passwords

    $('#password-repeat').hide();
    $('#passwordrepnew').blur(function () {
        var passwd = $('#passwordnew').val();
        var passwdrep = $('#passwordrepnew').val();
        if (passwd === passwdrep) {
            $('#password-repeat').hide();
        } else {
            $('#password-repeat').show();
        }
    });

    //modal-button "cambiarClave"
    $("#btnEnviar").click(function () {
        var passwd = $('#passwordnew').val();
        var passwdrep = $('#passwordrepnew').val();

        if (passwd === passwdrep && passwd !== '' && passwdrep !== '') {
            $("#validationModal").modal('show');
            $("#msgSuccessModal").show();
            $("#textModal").text("Cambio de clave exitoso.");
            // $("#msgErrorModal").hide();
            $("#textModalError").hide();

        } else {
            $("#validationModal").modal('show');
            $("#msgErrorModal").show();
            $("#textModal").text("No se ha podido cambiar clave.");
            // $("#msgSuccessModal").hide();
            $("#textModalSuccess").hide();
        }


    });


});
