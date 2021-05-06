function CheckTriggerHorarioBox() {

    if ($(this).attr("value") === "1") {
        $(".HorarioBox").hide('slow');
    }
    if ($(this).attr("value") === "2") {
        $(".HorarioBox").show('slow');
    }
}

function validarHorarioBox() {
    // Si el día esta marcado, validar las horas
    let atLeastOne;
    atLeastOne = false
    $diasHorario = document.querySelectorAll(".diaHorario")
    $diasHorario.forEach(function (currentValue, currentIndex, listObj) {
        $dia = $(currentValue).children('.dia');

        $horaApertura = $(currentValue).children('.horaApertura')
        $horaCierre = $(currentValue).children('.horaCierre')

        $diaForm = $dia.children('.diaForm');
        $input = $diaForm.children('.form-check-input')[0];


        if ($input.checked) {
            atLeastOne = true
            $form = $horaApertura.children('.horaAperturaForm')
            $horaAperturaValue = moment($form.children('input')[0].value, 'hh:mm')

            $form = $horaCierre.children('.horaCierreForm')
            $horaCierreValue = moment($form.children('input')[0].value, 'hh:mm')

            if ($horaCierreValue._i === '' || $horaAperturaValue._i === '') {
                // Must show alerta for field not completed

                $("#msgErrorHorario")[0].style.display = "block"
            } else {
                $("#msgErrorHorario")[0].style.display = "none"
            }


            if ($horaAperturaValue > $horaCierreValue) {
                // Must show alerta for Apertura < Cierre

                $("#msgAperturaMayor")[0].style.display = "block"
            } else {
                $("#msgAperturaMayor")[0].style.display = "none"
            }

        }
    });
    if (atLeastOne === false) {

        $("#msgSinOpcionElegida")[0].style.display = "block"
    } else {
        $("#msgSinOpcionElegida")[0].style.display = "none"
    }

}

function validarFormTipoReciclag() {
    var selected = false
    $formTipoRecilagList = document.querySelectorAll(".formTipoReciclag")
    $formTipoRecilagList.forEach(function (currentValue,
                                           currentIndex,
                                           listObj) {
            if ($(currentValue).children('input')[0].checked) {
                selected = true
            }
        }
    );

    if (selected === false) {
        $("#msgErrorMateriales")[0].style.display = "block"

    } else {
        $("#msgErrorMateriales")[0].style.display = "none"

    }
}

function mapAddress(mapElement, address) {
    var geocoder = new google.maps.Geocoder();
    var result;
    geocoder.geocode({'address': address}, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            var mapOptions = {
                zoom: 16,
                center: results[0].geometry.location,
                disableDefaultUI: true
            };
            var map = new google.maps.Map(mapElement.children('.map_canvas')[0], mapOptions);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });



        } else {
            alert("Geocode was not successful for the following reason: " + status);

        }

    });
    console.log(result)
    return result
}


$(document).ready(function () {
    console.log("Hello World -- Main executed")

    // HORARIO
    // Check if horario exists and load script
    if ($('.horario')[0]) {
        $("#opcionHorario1").trigger('click');
        // CHECK IF HORARIO MUST BE TRIGGERED
        $(".opcionHorario").click(CheckTriggerHorarioBox);
    }

    // ON INSCRIBIR O MODIFICAR PUNTO ............
    $("#inscribir").click(function () {
        //  Valida el HorarioBox
        if ($("#opcionHorario2")[0].checked) {
            validarHorarioBox()
        }
        // Valida los tipo de punto de reciclaG
        validarFormTipoReciclag()
    });

    // INICIATIVAS PAGE API CONSUMPTION
    $puntoContent = document.querySelectorAll(".punto_content")
    $puntoContent.forEach(function (currentValue, currentIndex, listObj) {
        // GOOGLE MAPS AND CLIMA CONSUMPTION API
        $puntoInformation = $(currentValue).children('.punto_information');
        $puntoInformationBody = $puntoInformation.children('.card-body')
        $cardText = $puntoInformationBody.children('.card-text')

        $direccionPuntoRerciclag = $cardText.children('.direccionPuntoReciclag').text()
        $temperaturePunto = $cardText.children('.temperaturaPunto')

        mapAddress($(currentValue), $direccionPuntoRerciclag.concat(" Chile"));

        var geocoder = new google.maps.Geocoder();

        geocoder.geocode({'address': $direccionPuntoRerciclag}, function (results, status, document) {

            $lat = results[0].geometry.location.lat()
            $lng = results[0].geometry.location.lng()

            jQuery.get('https://api.openweathermap.org/data/2.5/weather?lat='+$lat+'&lon='+$lng+'&exclude=hourly,daily&appid=c4cff409a04c1a3b55349f77cd26d0dd&lang=sp&units=metric',
                function(data) {
                    $temperaturePunto[0].innerHTML = "Temperatura: "+data.main.temp+" grados - "+data.weather[0].description

                })


        });



    });
});