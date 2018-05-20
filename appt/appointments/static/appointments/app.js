$( document ).ready(function() {
  $("#new").click( function(event) {
    $(".toggleHide").toggleClass("hidden");
  });
  $("#cancel").click( function(event) {
    $(".toggleHide").toggleClass("hidden");
  });

  $("#search").click( function(event) {
    $(".added").html("");
    var params = $("#searchInput").val();
    event.preventDefault();
    getAppointments(params);
    $("#searchInput").val("");
    });
  $("#addAppointment").click( function(event) {
    $("#newAppointment").submit();
  })
});



function getAppointments(params) {
  $.get( "search/", {params: params}, function( data ) {
    var appointments = data.appointments;
    var appointmentsLength = appointments.length;
    var rows = "";
    for (var i = 0; i < appointmentsLength; i++) {
      var date = new Date(appointments[i].datetime);
      var date = ($.format.date(appointments[i].datetime, "MMM d"));
      var time = ($.format.date(appointments[i].datetime, "h:mmp"));
      var row = "<tr class='added'><td>" + date + "</td><td>" + time + "</td><td>"+ appointments[i].description + "</td></tr>";
      rows = rows + row;
    }
    $("#results").after(rows);
  });
}
