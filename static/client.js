/*this file for client code on javascript*/
function checkParams() {
    var email = $('#email').val();
    var pas = $('#pas').val();

    if(email.length != 0 && pas.length != 0) {
        $('#buttonSignIn').removeAttr('disabled');
    } else {
        $('#buttonSignIn').attr('disabled', 'disabled');
    }
}