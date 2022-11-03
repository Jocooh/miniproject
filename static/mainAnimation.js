$(document).ready(function (){

    $(window).scroll(function (){
        const scrollTop = $(document).scrollTop();

        if(scrollTop >= 350){
            $('#msg1').addClass('on');
        } else if(scrollTop < 350){
            $('#msg1').removeClass('on');
        }

        if(scrollTop >= 750){
            $('#msg2').addClass('on');
        } else if(scrollTop < 750){
            $('#msg2').removeClass('on');
        }
    })
});

