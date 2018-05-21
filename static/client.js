$("#regButton").click(function() {
    $("#myModalBox").modal('show');
});
function checkPass() {//мне пока видится решение через костыли, как закрыть поле
    var pas1 = $('#pas1').val();//пароля звездочками и при этом обрабатывать его в коде
    var pas2 = $('#pas2').val();//попрбуй найти решение без костылей
    if (pas1 == pas2) {
        $('#reg').removeAttr('disabled');
        }
        else {
        $('#reg').attr('disabled', 'disabled');
        }
}
function logOut() {
    $.removeCookie('session', { path: '127.0.0.1:8000/landing/' });
    $.removeCookie('session', { path: '127.0.0.1:8000/home/' });
    $.cookie('session', null);
    $.cookie('session', null, { path: '127.0.0.1:8000/landing/' });
   var session = $.cookie('session')
   //alert(session)
    window.location.replace("http://127.0.0.1:8000/logout/");
}