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
//Catalogue
}

function isBuilder(){
//isBuilder
}

function feedback(){
//feedback
}