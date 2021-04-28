

$(document).ready(function () {
    //show div "Box"
    $('input[type="radio"]').click(function () {
        if ($(this).attr("value") != "2") {
            $(".Box").hide('slow');
        }
        if ($(this).attr("value") == "2") {
            $(".Box").show('slow');

        }
    });
    //$('input[type="radio"]').trigger('click');  // trigger the event
    //alerts

});



