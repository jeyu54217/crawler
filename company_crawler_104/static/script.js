// datatable
 $(document).ready(function() {
    $('#datatable').DataTable();
} );

//  search-table
$('#addRowChild').click(function(){
    // window.alert('GO!');
    $('#search-table tbody').append(`<tr>${$('#default-row').html()}</tr>`);
});

$('#btn_search_submit').click(function(){
    // get all keyword value from html class name
    var kwyword_ary = Array();
    kwyword_ary.push($('.form-control').map(function(){
        return this.value
    }).get());

    var data_for_post = {
        'key_of_kwyword_list[]' : kwyword_ary  // must add [] as key
    };

    var data_post = $.post('http://127.0.0.1:8000/search/', data_for_post);
    // redirect current page
    $.when(data_post).done(function(){
        window.location.href="http://127.0.0.1:8000/search/";
    });
 });



 $('#btn_selected_submit').click(function(){
    var checked_ary = Array();
    checked_ary.push($('[name^="checkbox_"]:checked').map(function(){
        return $(this).attr('name')
    }).get());

    var data_for_post_ = {
        'key_of_checked_list[]' : checked_ary
    };
    var data_post_ = $.post('http://127.0.0.1:8000/selected/', data_for_post_);
 });

//  $('#checkbox-value').text($('#checkbox1').val());

//  $("#checkbox1").on('change', function() {
//    if ($(this).is(':checked')) {
//      $(this).attr('value', 'true');
//    } else {
//      $(this).attr('value', 'false');
//    }
   
//    $('#checkbox-value').text($('#checkbox1').val());
//  });



