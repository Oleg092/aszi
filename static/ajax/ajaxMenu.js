function getReqList(fName){ //запрос списка требований и передача их в функцию обработки
    $.ajax({
        url: 'http://127.0.0.1:8000/get_req_list/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var reqList = JSON.parse(data);
            if (fName == "pageCatalogueLink"){
                catalogue(reqList);
            }
            if (fName == "pageManagementLink"){
                management(reqList);
            }
        },
        failure: function(data) {

        }
    });
}

function catalogue(reqList){
    $.ajax({
        url: 'http://127.0.0.1:8000/getSziList/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var sziList = JSON.parse(data);
            catalogReq(sziList, reqList);

        },
        failure: function(data) {

        }
    });
}

function feedback(){
//feedback
}
function management(reqList){
    $("#requirCheck").empty();
    console.log(reqList.length);
    console.log(reqList[1]["fields"]["description"])
    for(i=0; i < reqList.length; i++){
        mess = '<H3>'+reqList[i]["fields"]["require"]+'</H3>'+reqList[i]["fields"]["description"]+'';
        label = '<label id="'+mess+'" onmouseover="descShow(id)" class="form-check-label" for="inlineFormCheck'+i+'">'+reqList[i]["fields"]["require"]+'</label>';
        $("#requirCheck").append('<input id="inlineFormCheck'+i+'" type="checkbox" class="form-check-input" value="'+reqList[i]["pk"]+'">'+label+'<Br>');

    }
}

function catalogReq(sziList, reqList){
    $("#pageCatalogue1").empty();
    var catalog;
    var labelDesc;
    var idReq;
    for(i = 0; i < sziList.length; i++){//вывод сзи на страницу catalogue
        labelDesc = '<div class = "descSzi"><h5>Szi Description</h5>'+sziList[i]["fields"]["def_desc"]+'</div>'
        catalog = '<div id="szi'+i+'" class="sziInCatalogue"><div class="sziInfo"><h5>Szi Info</h5>'+sziList[i]["fields"]["def_name"]+'</br>'+sziList[i]["fields"]["def_dev"]+'</br><label>Сертефицирован до: <label>'+sziList[i]["fields"]["def_cert"]+'</div>'+labelDesc+'</div>';
        $('#pageCatalogue1').append(catalog);
    }
    var req = '';
    $("#requirCheck").empty();
    for(i=0; i < sziList.length; i++){// пробегаемся по всем сзи
        for(j=0; j < sziList[i]["fields"]["requirements"].length; j++){//а теперь по всем реквариментсам которые они покрывают
            idReq = sziList[i]["fields"]["requirements"][j];
            req += '<h6>'+reqList[idReq]["fields"]["require"]+'</h6>'+reqList[idReq]["fields"]["description"]+'<br><br>';
        }
        reqListInCat = '<div class="sziReqCatalogue"><h5>Requirements List</h5>'+req+'</div>';
        $("#szi"+i+"").append(reqListInCat);
        req = '';
    }
}

function getUserList(){
    $.ajax({
        url: 'http://127.0.0.1:8000/getUserList/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var userList = JSON.parse(data);
            showUsers(userList);

        },
        failure: function(data) {

        }
    });
}

function showUsers(userList){
    console.log(userList);
}