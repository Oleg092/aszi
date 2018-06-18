var activePage = "pageProfile";

$("#regButton").click(function() {
    $("#myModalBox").modal('show');
});

function togl(idLink){
	idLink = idLink.substr(0, idLink.length - 4);
	tooglePage(idLink);
}

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
   var session = $.cookie('session');
   //alert(session)
    window.location.replace("http://127.0.0.1:8000/logout/");
}

function tooglePage(name_page){
    $(".menu").hide();
    $("#"+name_page+"").show();
}

function descShow(desc){       //отображение описания requirements при наведении на стр management
    $('#descReq').html(desc);
}

function checkBoxShow(type){// доступность чекбоксов на 2ой странице алгоритма подбора
    if (type != 'checkSziOnPr'){
        if ($('#'+type+'').prop("checked") == true){
            $('.'+type+'').removeAttr('disabled'); //чекбоксы доступны
        }
        else{
            $('.'+type+'').attr('disabled', 'disabled'); //не доступны
            $('.'+type+'').prop("checked", false); // если чекбоксы были включены то отключаем
        }
    }
    else{
        if ($('#checkSziOnPr').prop("checked") == true){//если в системе есть сзи, показываем пользователю форму с сзи
            $('#sziOnPr').show();
        }
        else{//иначе скрываем ее
            $('#sziOnPr').hide();
        }
    }
}