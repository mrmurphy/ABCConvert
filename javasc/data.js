function writeOut(message){
    var origtext = $('#output_text').html();
    $('#output_text').html(origtext + "<br>" + message);
    setTimeout(function(){writeOut(message)}, 1000);
}

$("input#go_button").click(function(event){
    var fval = $('#shot_field').val();
    $.ajax("http://localhost:8080/"+"NewConvert/"+fval);
    $.getJSON("http://localhost:8080/CheckStatus", function(data){
        alert(data.stats);
    });
});
