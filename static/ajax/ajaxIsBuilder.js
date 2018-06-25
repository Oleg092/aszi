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
            var sziList = JSON.parse(data);
            console.log(sziList)
            showSziOnPage(sziList)
        },
        failure: function(data) {
            console.log('Bad request');
        }
    });
}

function showSziOnPage(sziList){
    $("#buildSzi").empty();
    $("#myModalBox").modal('show');
    var catalog;
    var labelDesc;
    var coast = '';
    var ct='';
    var ct2='';
    var sumct='';
    let sum = 0;
    let coast1 = 13100;
    let coast2 = 30000;
    var allSum = 0;
    for(i = 0; i < sziList.length; i++){//вывод сзи на страницу resultBuild
        if (sziList[i]["fields"]["def_os"] == 0) {
            labelDesc = '<div class = "descSzi"><h5>Szi Description</h5>'+sziList[i]["fields"]["def_desc"]+'</div>'
            catalog = '<div id="sziC'+i+'" class="sziInCatalogue"><div class="sziInfo"><h5>Szi Info</h5>'+sziList[i]["fields"]["def_name"]+'</br>'+sziList[i]["fields"]["def_dev"]+'</br><label>Сертефицирован до: <label>'+sziList[i]["fields"]["def_cert"]+'</div>'+labelDesc+'</div>';
            $('#buildSzi').append(catalog);
        }
        coast1 = coast1 * (i+1);
        coast2 = coast2 * (i+1);
        sum = coast1 + coast2;
        ct = '<h6>Стоимость СрЗИ</h6>'+coast1+' rub<br><h6>Стоимость тех поддержки</h6>'+coast2+' rub';
        sumct = '<h6>Общая стоимость</h6>'+sum+' rub';
        reqListInCat = '<div class="sziReqCatalogue"><h5 style = "position: sticky; top: 0px; background: white;">Coast List</h5>'+ct + sumct +'</div>';
        $("#sziC"+i+"").append(reqListInCat);
        allSum += sum

    }
    $('#allSum').append('<h5>Общая стоимость внедрения:</h5>'+allSum+' rub')
}