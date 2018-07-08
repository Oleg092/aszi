function getReqList(fName){ //запрос списка требований и передача их в функцию обработки
    $.ajax({
        url: 'http://127.0.0.1:8000/get_req_list/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var reqList = JSON.parse(data);
            if ((fName == "pageCatalogueLink")||(fName == 'pageBuilderLink')){
                catalogue(reqList, fName);
            }
            if (fName == "pageManagementLink"){
                management(reqList);
            }
            if (fName == "pageMeasuresLink"){
                measures(reqList);
            }
        },
        failure: function(data) {

        }
    });
}

function catalogue(reqList, fName){
    $.ajax({
        url: 'http://127.0.0.1:8000/getSziList/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var sziList = JSON.parse(data);
            if (fName != 'pageBuilderLink'){
                catalogReq(sziList, reqList);
            }
            else {
                buildData(sziList, reqList);
            }

        },
        failure: function(data) {

        }
    });
}

function feedback(){
//feedback
}
function management(reqList){ // вывод спискасписок реквариментов для страницы management
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
    var req = '';
    $("#requirCheck").empty();
    var catalog;
    var labelDesc;
    var idReq;
    for(i = 0; i < sziList.length; i++){//вывод сзи на страницу catalogue
        if (sziList[i]["fields"]["def_os"] == 0) {
            labelDesc = '<div class = "descSzi"><h5>Szi Description</h5>'+sziList[i]["fields"]["def_desc"]+'</div>'
            catalog = '<div id="szi'+i+'" class="sziInCatalogue"><div class="sziInfo"><h5>Szi Info</h5>'+sziList[i]["fields"]["def_name"]+'</br>'+sziList[i]["fields"]["def_dev"]+'</br><label>Сертефицирован до: <label>'+sziList[i]["fields"]["def_cert"]+'</div>'+labelDesc+'</div>';
            $('#pageCatalogue1').append(catalog);
        }
        for(j=0; j < sziList[i]["fields"]["requirements"].length; j++){//а теперь по всем реквариментсам которые они покрывают
            idReq = sziList[i]["fields"]["requirements"][j];
            req += '<h6>'+reqList[idReq]["fields"]["require"]+'</h6>'+reqList[idReq]["fields"]["description"]+'<br><br>';
        }
        reqListInCat = '<div class="sziReqCatalogue"><h5 style = "position: sticky; top: 0px; background: white;">Requirements List</h5>'+req+'</div>';
        $("#szi"+i+"").append(reqListInCat);
        req = '';
    }

}

let UserList = () => {
    $.ajax({
        url: 'http://127.0.0.1:8000/getUserList/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var userList = JSON.parse(data);
            showUsers(userList)

        },
        failure: function(data) {

        }
    });
};

function showUsers(userList){ // вывод списка юзеров
    let users = userList;
    $('#userListR').empty();
    let user;
    let email;
    let firstName;
    let lastName;
    let btn;
    console.log(users);
    for(i=0; i < users.length; i++){
        email = '<div class = "userList"><label>'+users[i]["fields"]["email"]+'</label></div>';
        firstName = '<div class = "userList"><label>'+users[i]["fields"]["firstname"]+'</label></div>';
        lastName = '<div class = "userList"><label>'+users[i]["fields"]["lastname"]+'</label></div>';
        btn = '<div class="userList" id="'+users[i]["pk"]+'"><button class="btn">Edit</button></div>';
        user = '<div class="userListR">' + email + firstName + lastName + btn + '</div>';
        $('#userListR').append(user);
    }
}

function buildData(sziList, reqList){
    let osOnCl;
    let osOnSer;
    $("#sziOnPr").empty();
    $('#osOnClient').empty();
    $('#osOnServer').empty();
    for(i = 0; i < sziList.length; i++){//вывод сзи на страницу build
        if (sziList[i]["fields"]["def_os"] == 1) {
            console.log(i);
            osOnCl = '<input id="inlineFormCheck'+sziList[i]["pk"]+'" type="checkbox" style = "position: relative; left 5px; class="form-check-input listOsCheck1" value=""><label>'+sziList[i]["fields"]["def_name"]+'</label><br>';
            $('#osOnClient').append(osOnCl);
        }
        if (sziList[i]["fields"]["def_os"] == 2) {
            console.log(i);
            osOnSer = '<input id="inlineFormCheck'+sziList[i]["pk"]+'" type="checkbox" style = "position: relative; left 5px; class="form-check-input listOsCheck1" value=""><label>'+sziList[i]["fields"]["def_name"]+'</label><br>';
            $('#osOnServer').append(osOnSer);
        }
        if (sziList[i]["fields"]["def_os"] == 0) {
            label = '<H3>'+sziList[i]["fields"]["def_name"]+'</H3>';
            $("#sziOnPr").append('<input id="inlineFormCheck'+sziList[i]["pk"]+'" type="checkbox" class="form-check-input" value="'+sziList[i]["pk"]+'">'+label+'<Br>');
        }
    }
}

function measures(reqList){//вывод список реков на страницу measures
    $('#reqListR').empty();
    var req;
    var require;
    var description;
    var pdn_lvl;
    for(i=0; i < reqList.length; i++){
        require = '<div class = "reqList"><label>'+reqList[i]["fields"]["require"]+'</label></div>';
        description = '<div style="position: relative; width: 75%;" class = "reqList"><label>'+reqList[i]["fields"]["description"]+'</label></div>';
        pdn_lvl = '<div class = "reqList"><label>'+reqList[i]["fields"]["pdn_lvl"]+'</label></div>';
        req = '<div class="reqListR">' + require + description + pdn_lvl + '</div>';
        $('#reqListR').append(req);
    }
}