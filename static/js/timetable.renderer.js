$(document).ready(function () {
    $("#side-calendar").datepicker({
        dateFormat: 'yy-mm-dd',
        onSelect: function (date) {
            $.ajax({
                url: '/schedule/get_schedule_list/'+date+"/",
                success: function (data) {
                    if (data.staff.length === 0 || data.employee.length === 0){
                        $('.timetable').html('<div class="alert alert-danger">На сегодня нет графика работы!</div>')
                    } else {
                        var location = [];
                        var event = [];
                         $.each(data.employee, function (key, value) {
                             location.push(value)
                         });
                         $.each(data.events, function (key, value) {
                             event.push(value)
                         });
                         getTimetable(location, event);
                    }
                },
                error: function (error) {
                    console.log(error)
                }
            })
        }
    });
    var date_now = Date.now();
    $.ajax({
        url: '/schedule/get_schedule_list/'+ moment(date_now).format('YYYY-MM-DD') +'/',
        success: function (data) {
            if (data.staff.length === 0 || data.employee.length === 0){
                $('.timetable').html('<div class="alert alert-danger">На сегодня нет графика работы!</div>')
            } else {
                var location = [];
                var event = [];
                 $.each(data.employee, function (key, value) {
                     location.push(value)
                 });
                 $.each(data.events, function (key, value) {
                     event.push(value)
                 });
                 getTimetable(location, event);
            }
        },
        error: function (error) {
            console.log(error)
        }
    });
    });

    function getTimetable(location, event) {
    var timetable = new Timetable(location);
    timetable.setScope(8, 21);
    timetable.addLocations(location);
    $.each(event, function (key, value) {
       //timetable.addEvent('Test event', 'John Doe', new Date(2018, 2, 7, 16, 0), new Date(2018, 2, 7, 18, 0))
        var valid_date = value.start_event.toDateFormDatetime();
        var end_date = value.end_event.toDateFormDatetime();
        /*
        var date = value.start_event.split('-');
        var time = value.start_event.split(':');
        */
        var get_year = parseInt(valid_date['0']);
        var get_month = parseInt(valid_date['1']);
        var get_day = parseInt(valid_date['2']);
        var get_hour = parseInt(valid_date['3']);
        var get_minute = parseInt(valid_date['4']);

        var end_year = parseInt(end_date['0']);
        var end_month = parseInt(end_date['1']);
        var end_day = parseInt(end_date['2']);
        var end_hour = parseInt(end_date['3']);
        var end_minute = parseInt(end_date['4']);

        /*
        var get_year = valid_date.getFullYear();
        console.log("Year: "+get_year);
        var get_month = valid_date.getMonth();
        console.log("Month: " + get_month);
        var get_day = valid_date.getDate();
        console.log("Day: "+get_day);
        var get_hour = valid_date.getHours();
        console.log("Hours: "+get_hour);
        var get_minute = valid_date.getMinutes();
        console.log("Minutes: "+get_minute);
        */
        timetable.addEvent('Стрижка уточок', location[key], new Date(get_year, get_month, get_day, get_hour+2, get_minute), new Date(end_year, end_month, end_day, end_hour+2, end_minute));
    });
    timetable.addEvent('Fly', 'Elon Musk', new Date(2018, 2, 7, 12, 30), new Date(2018, 2, 7, 14, 0));
    var renderer = new Timetable.Renderer(timetable);
    renderer.draw(".timetable")
    }