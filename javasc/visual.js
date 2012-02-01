$(document).ready(function(){
    /// Establish some global variables:
    var out = $('#output');
    var outtext = $('#output_text');
    var ui = $('#ui');
    var logmessage = "";

    // Give the field a default value:
    $('#shot_field').focus(function() {  
        if (this.value == this.defaultValue){  
            this.value = '';  
        }  
        if(this.value != this.defaultValue){  
            this.select();  
        }  
    });  

    // On button click, make the output div animate open.
    $("input#go_button").click(function(event){
        event.preventDefault();
        var shotname = $('#shot_field').val();
        F_openOutput();
    });
    // Handle event for reset button;
    var resetbutton = $('#reset_button');
    resetbutton.click(function(event){
        $("#inputdiv").slideToggle(100);
        event.preventDefault();
        out.slideToggle(100, function(){
            ui.center({transition:100})
        });
    });

    F_writeOutText = function(text){
       var message = text + "<br>"+logmessage;
       outtext.html(message);
    }

    var F_openOutput = function(){
        $("#inputdiv").slideToggle(100);
        out.slideToggle(100, function(){
            ui.center({transition:100})
        });
    }

    // Hide the output box.
    $('#output').hide();
    // I don't know why I have to do this twice..
    ui.center();

    // Center on window resize.
    $(window).bind('resize', function() {
        ui.center();
    });
});

