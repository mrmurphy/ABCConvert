Titanium.include("python/sleep.py");

function writeOut(message){
        var origtext = $('#output_text').html();
        $('#output_text').html(origtext + "<br>" + message);
}

$("input#go_button").click(function(event){
    var foo = Shot("asdf");
    foo.start();
});
