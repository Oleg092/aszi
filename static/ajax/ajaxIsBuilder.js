function tglBuilMenuPg(Page){// работа кнопочек навигационного меню
    $('#nextPage').show();
    $('#sendData').hide();
    var flag;
    var i = 1;
    if (Page == 'next'){
        while (i < 4){
            if($('#flag'+i+'').html() == 'active'){
                console.log(i);
                break;
            }
            i++;
        }
        if ((i == 1) || (i == 2)){
            Page = i + 1;
        }
        else{

        }
    }
    console.log(Page);
    flag = '#flag';
    var content;
    content = '#buildLevel';
    content += Page;
    flag += Page;
    $('.dataBuild').hide()
    $(content).show();
    $('.flag').html('no active')
    $(flag).html('active')
    if ($('#flag3').html() == 'active'){
        $('#nextPage').hide();
        $('#sendData').show();
    }
}




function buildSziList(){ //отправка запроса на сервер
    let n = 51;
    let i = 1;
    let count = 0;
    let idSzi = '';
    let idList = [];
    let pdnLevel = $('#defLevel').val();
    let amountArm = $('#amountArm').val();
    let amountServ = $('#amountServ').val();
    let listOsCheck;
    /*structure*/
    let notUsingWireless = () => {
        if ($('#notUsingWireless').is(':checked') == true) return "True"
        if ($('#notUsingWireless').is(':checked') == false) return ""//пятон будет преобразовывать это в false
    }
    let notUsingMobile = () => {
        if ($('#notUsingMobile').is(':checked') == true) return "True"
        if ($('#notUsingMobile').is(':checked') == false) return ""
    }
    let notUsingVirtual = () => {
        if ($('#notUsingVirtual').is(':checked') == true) return "True"
        if ($('#notUsingVirtual').is(':checked') == false) return ""
    }
    /*szi*/
    while (i < n){ // выясняем, какие сзи есть в системе
        if ($('#inlineFormCheck'+i).is(':checked') == true){
            idSzi = $('#inlineFormCheck'+i).attr('id');
            console.log(idSzi.substr(15));
            idList[count] = idSzi.substr(15);
            count++;
        }
        i++;
    }
    $.ajax({
        url: 'http://127.0.0.1:8000/build_szi_list/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                listSzi: idList,
                pdnLevel: pdnLevel,
                amountArm: amountArm,
                amountServ: amountServ,
                notUsingWireless: notUsingWireless,
                notUsingMobile: notUsingMobile,
                notUsingVirtual: notUsingVirtual,

            },
        success: function(data) {

        },
        failure: function(data) {
            console.log('Bad request');
        }
    });
}