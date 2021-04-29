export function CheckTriggerHorarioBox() {

    if ($(this).attr("value") == "1") {
        $(".HorarioBox").hide('slow');
    }
    if ($(this).attr("value") == "2") {
        $(".HorarioBox").show('slow');

    }
};

export function ValidarHorarioBox() {
    // Nothing here
}