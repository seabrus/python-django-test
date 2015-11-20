
$( document ).ready( function() {

  function reloadNameFormEvents() {
    // Datepicker
    $( "#id_date_field" ).datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
    });
   // $( ".selector" ).datepicker( "option", { dateFormat: 'yy-mm-dd' } );

    // AJAX form
    $('#name_form').on('submit', function(e) {
        $('#loading_gif').toggle(500);
        var self = $( this );

console.log( self.serializeArray()[0] );
console.log( self.serializeArray()[1] );
console.log( self.serializeArray()[2] );

        $('#name_form_partial').load('/dj/your-name/', 
            self.serializeArray(),  
            function(response, status, xhr) {
                if ( status == 'error' ) {
                    var msg = 'Sorry but there was an AJAX error: ';
                    $( "#name_form_ajax_message" ).text( msg + xhr.status + ' ' + xhr.statusText ).removeClass('green').addClass('red');
                }

            $( "#name_form_ajax_message" ).text( 'The form was sent via AJAX successfully' ).removeClass('red').addClass('green');
            reloadNameFormEvents();
            $('#loading_gif').toggle(500);
        });
        
        e.preventDefault();
    });

  }

  reloadNameFormEvents();

});

