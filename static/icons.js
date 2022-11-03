$(document).ready(function (){

    // TOP 이동
    $('.top').on('click', function(){
      $('html, body').animate({scrollTop:0},200);
    })

    // 다크 모드
    $('.darkmode').on('click', function(e){
        $('html, body').toggleClass('dark');
        $('.msg').toggleClass('dark');
        $('.icons').toggleClass('dark');
        $('.goal').toggleClass('dark');
        $('.rule').toggleClass('dark');
        $('.introduce').toggleClass('dark');
        $('.desc').toggleClass('dark');
        $('.about').toggleClass('dark');
        $('.my_style').toggleClass('dark');
        $('.hi').toggleClass('dark');
        $('.board').toggleClass('dark');
        $('.nav_wrapper').toggleClass('dark');

    })
});
