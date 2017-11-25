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

    $('submit-new-event').click(function() {
        var startTime = $("#start_time").val()
        var endTime = $("#end_time").val()
        $.ajax ({
            url: '/add_event',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(window).resize(function() {
   var cw = $('.day-box').width();
    $('.day-box').css({'height':cw+'px'});
});
