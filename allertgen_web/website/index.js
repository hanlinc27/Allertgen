$( window ).resize(function() {
    $( "body" ).prepend( "<div>" + $( window ).width() + "</div>" );
  });