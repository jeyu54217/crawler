


//  search-table
 $('#addRowChild').click(function(){
    $('#search-table tbody').append(`<tr>${$('#default-row').html()}</tr>`);
 });

//  $('#delRowChild').click(function(){
//     var $('#search-table tbody')
//     $('#search-table tbody').delete(`<tr>${$('#default-row').html()}</tr>`);
//  });

 

// datatable
 $(document).ready(function() {
    $('#datatable').DataTable();
} );