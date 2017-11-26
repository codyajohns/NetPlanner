$(document).ready(function() {
    var cw = $('.day-box').width();
    $('.day-box').css({'height':cw+'px'});

    $('.menu .item') .tab() ;
    $('.dropdown').dropdown();
    $('.ui.modal').modal('show');

    $('#rangestart').calendar({
      endCalendar: $('#rangeend')
    });
    $('#rangeend').calendar({
      startCalendar: $('#rangestart')
    });

    $('#add-event-form').submit(function(e) {
        e.preventDefault();

        var start_epoch = document.getElementsByName("start_time")[0];
        var end_epoch = document.getElementsByName("end_time")[0];
        start_epoch.value = new Date (start_epoch.value).getTime();
        end_epoch.value = new Date (end_epoch.value).getTime();

        this.submit();
    });
});

$(window).resize(function() {
   var cw = $('.day-box').width();
    $('.day-box').css({'height':cw+'px'});
});
