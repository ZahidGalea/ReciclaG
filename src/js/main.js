import { triggerHorarioBox } from './modules/horarios.js';


$(document).ready(function () {
    console.log("Hello World -- Main executed")

    $("#opcionHorario1").trigger('click');
    //show div "HorarioBox"
    $(".opcionHorario").click(triggerHorarioBox);


});