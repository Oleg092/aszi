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
    var n = 90000;
    var i = 0;
    var pdnLevel = $('#defLevel').val();
    var amountArm = $('#amountArm').val();
    var amountServ = $('#amountServ').val();
    var listOsCheck;
    /*structure*/
    var notUsingWireless = $('#notUsingWireless').is(':checked');
    var notUsingMobile = $('#notUsingMobile').is(':checked');
    var notUsingVirtual = $('#notUsingVirtual').is(':checked');
    /*coast*/
    var licenseOnHost = $('#licenseOnHost').is(':checked');
    var technicalSupport = $('#technicalSupport').is(':checked');
    var teachingSlave = $('#teachingSlave').is(':checked');
    var acquisitionCost = $('#acquisitionCost').is(':checked');
    /*szi*/
    var sziList;
    var countOs = 2; //listOsCheck при добавлении ос прибавить
    alert(acquisitionCost);
    while (i < n){
        if ($('#inlineFormCheck'+i).val() == undefined){
            break;
        }
    console.log($('#inlineFormCheck'+i).is(':checked'));
    i++;
    }
}