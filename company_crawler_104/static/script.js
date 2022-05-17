


//  search-table

$('#addRowChild').click(function(){
    // window.alert('GO!');
    $('#search-table tbody').append(`<tr>${$('#default-row').html()}</tr>`);
});


$('#btn_summit').click(function(){
    // window.alert('Work!');
    var data_list = Array();
    data_list.push($('.form-control').map(function(){
         return this.value
        }).get());
    var data_save = {
        'data[]' : data_list
    };
    // let data_rsp = $.post('/crawler_core/main_crawler', data_save);
    var data_rsp = $.post('http://127.0.0.1:8000/search/', data_save);


 })



// datatable
 $(document).ready(function(data_list) {
    $('#datatable').DataTable();
} );


