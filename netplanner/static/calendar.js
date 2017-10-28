$(document).ready(function() {
    var cw = $('.day-box').width();
    $('.day-box').css({'height':cw+'px'});

    $('.menu .item') .tab() ;
    $('.dropdown').dropdown();
    $('.ui.modal').modal('show');
});

$(window).resize(function() {
   var cw = $('.day-box').width();
    $('.day-box').css({'height':cw+'px'});
});
