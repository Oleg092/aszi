function main(){
    var userId = $.cookie('user')
    $.ajax({
        url: 'http://127.0.0.1:8000/xhr_test/',
        type: 'POST',
        data:{
                userId: userId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var message = JSON.parse(data);
            //alert(message["name"]);
            //далее данные парсятся как в алерте, и подгружаются в соответствующие блоки на странице
        },
        failure: function(data) {
            alert('User Data Not Found');
        }
    });
}

function catalogue(){
    $.ajax({
        url: 'http://127.0.0.1:8000/getSziList/',
        type: 'POST',
        data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            //console.log(message[1]);
            catalogReq(data);

        },
        failure: function(data) {

        }
    });
}

function isBuilder(){
//isBuilder
}

function feedback(){
//feedback
}
function management(){
    var userId = $.cookie('user')
    $.ajax({
        url: 'http://127.0.0.1:8000/get_management_data/',
        type: 'POST',
        data:{
                userId: userId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
        success: function(data) {
            var message = JSON.parse(data);
            $("#requirCheck").empty();
            console.log(message.length);
            console.log(message[1]["fields"]["description"])
            for(i=0; i < message.length; i++){
                mess = ''+message[i]["fields"]["description"]+'';
                console.log(mess)
                label = '<label id="'+mess+'" onmouseover="descShow(id)" class="form-check-label" for="inlineFormCheck'+i+'">'+message[i]["fields"]["require"]+'</label>';
                //$("#id_requirements").append( $('<option style="height: 30px; width: 100px;" value="'+message[i]["pk"]+'">'+message[i]["fields"]["require"]+'</option>'));
               $("#requirCheck").append('<input id="inlineFormCheck'+i+'" type="checkbox" class="form-check-input" value="'+message[i]["pk"]+'">'+label+'<Br>');

            }
        },
        failure: function(data) {

        }
    });
}

function catalogReq(data){
    var ms = JSON.parse(data);
    var catalog;
    $("#pageCatalogue1").empty();
    for(i = 0; i < ms.length; i++){//вывод сзи на страницу catalogue
        console.log(ms[i]);
        labelDesc = '<div class = "descSzi"><h5>Szi Description</h5>'+ms[i]["fields"]["def_desc"]+'</div>'
        catalog = '<div id="szi'+i+'" class="sziInCatalogue"><div class="sziInfo"><h5>Szi Info</h5>'+ms[i]["fields"]["def_name"]+'</br>'+ms[i]["fields"]["def_dev"]+'</br><label>Сертефицирован до: <label>'+ms[i]["fields"]["def_cert"]+'</div>'+labelDesc+'</div>';
        $('#pageCatalogue1').append(catalog);
    }
    $.ajax({
        url: 'http://127.0.0.1:8000/get_management_data/',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data) {
            var message = JSON.parse(data);
            var req = '';
            $("#requirCheck").empty();
            console.log(message.length);
            console.log(message[1]["fields"]["description"])
            for(i=0; i < ms.length; i++){
                //reqListInCat='';
                for(j=0; j < ms[i]["fields"]["requirements"].length; j++){
                    idReq = ms[i]["fields"]["requirements"][j]
                    req += '<h6>'+message[idReq]["fields"]["require"]+'</h6>'+message[idReq]["fields"]["description"]+'<br><br>';
                }
                reqListInCat = '<div class="sziReqCatalogue"><h5>Requirements List</h5>'+req+'</div>';
                $("#szi"+i+"").append(reqListInCat);
                req = '';
            }
        },
        failure: function(data) {

        }
    });
}