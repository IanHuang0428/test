$(document).ready(function(){

    $('#submit').click(function(){
        
        $.ajax({
            headers: { 'X-CSRFToken': csrf_token },
            type: 'POST',
            url: '/web_tool/screen_input/', 
            data: $('#transcript_form').serialize(),
            success: function(response){ 
            // $("#information").html('<div>'+response.correlation+'</div>'                    
            // );

            var obj = {
                rangeSelector: {
                selected: 1
                },
    
                title: {
                text: 'Stock Price'
                },
    
                series: [{
                name: response.stock1,
                data: response.stock1_response,
                tooltip: {
                    valueDecimals: 2
                }
                },{
                name: response.stock2,
                data: response.stock2_response,
                tooltip: {
                    valueDecimals: 2
                }
                }]}
    
            Highcharts.stockChart('container', obj);

            },
            error: function(){
                alert('Something error');
            },
        });
    });
});

