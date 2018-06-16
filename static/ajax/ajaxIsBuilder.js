function tglBuilMenuPg(Page){
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
            alert("отправка данных")
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
}




function buildSziList(){
    //not release
}