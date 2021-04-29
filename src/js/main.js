import { CheckTriggerHorarioBox } from './modules/horarios.js';


$(document).ready(function () {
    console.log("Hello World -- Main executed")
    /*
    * Renderization Part
    */

    // HORARIO
    $("#opcionHorario1").trigger('click');
    // CHECK IF HORARIO MUST BE TRIGGERED
    $(".opcionHorario").click(CheckTriggerHorarioBox);


});