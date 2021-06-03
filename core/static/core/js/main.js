function CheckTriggerHorarioBox() {

    if ($(this).attr("value") === "1") {
        $(".HorarioBox").hide('slow');
    }
    if ($(this).attr("value") === "2") {
        $(".HorarioBox").show('slow');
    }
}


function validarFormTipoReciclag() {
    var selected = false
    $formTipoRecilagList = document.querySelectorAll("#div_id_material_*")
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

    $("#submit-id-submit").click(function () {
        // Valida los tipo de punto de reciclaG
        validarFormTipoReciclag()
    });

    var geocoder = new google.maps.Geocoder();
    // INICIATIVAS PAGE API CONSUMPTION
    $puntoContent = document.querySelectorAll(".punto_content")
    $puntoContent.forEach(function (currentValue, currentIndex, listObj) {
        // GOOGLE MAPS AND CLIMA CONSUMPTION API
        $puntoInformation = $(currentValue).children('.punto_information');
        $puntoInformationBody = $puntoInformation.children('.card-body')
        $cardText = $puntoInformationBody.children('.card-text')

        $direccionPuntoRerciclag = $cardText.children('.direccionPuntoReciclag').text()
        $direccionPuntoRerciclagReg = $cardText.children('.direccionPuntoReciclagReg').text()
        $direccionPuntoRerciclagCom = $cardText.children('.direccionPuntoReciclagCom').text()
        $temperaturePunto = $cardText.children('.temperaturaPunto')

        $fulladdress = $direccionPuntoRerciclag.concat(" ", $direccionPuntoRerciclagCom, " ", $direccionPuntoRerciclagReg, " Chile")
        mapAddress($(currentValue), $fulladdress);

        geocoder.geocode({'address': $fulladdress}, function (results, status, document) {

            $lat = results[0].geometry.location.lat()
            $lng = results[0].geometry.location.lng()

            jQuery.get('https://api.openweathermap.org/data/2.5/weather?lat=' + $lat + '&lon=' + $lng + '&exclude=hourly,daily&appid=c4cff409a04c1a3b55349f77cd26d0dd&lang=sp&units=metric',
                function (data) {
                    $temperaturePunto[0].innerHTML = data.main.temp + " grados - " + data.weather[0].description

                })


        });


    });
});