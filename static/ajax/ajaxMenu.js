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
            var message = JSON.parse(data);
            var catalog;
            //$("#pageCatalogue1").empty();
            for(i = 0; i < message.length; i++){
                console.log(message[i]);
                catalog = '<div id="szi'+i+'" class="sziInCatalogue">'+message[i]["pk"]+'</br>'+message[i]["fields"]["def_name"]+'</br>'+message[i]["fields"]["def_dev"]+'</div>';
                $('#pageCatalogue1').append(catalog);
            }
            //console.log(message[1]);

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
            $("#id_requirements").empty();
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
