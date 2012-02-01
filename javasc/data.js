function writeOut(message){
    //var origtext = $('#output_text').html();
    $('#output_text').html(message);
}

function process_progress(){
    $.getJSON("http://localhost:8080/CheckShot", function(data){
        writeOut(data.log);
        if(data.finished !== "True"){
            setTimeout(function(){process_progress()}, 1000);
        }
    });
}

$("input#go_button").click(function(event){
    var fval = $('#shot_field').val();
    $.ajax("http://localhost:8080/"+"NewConvert/"+fval);
    process_progress();
});
