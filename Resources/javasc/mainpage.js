$(document).ready(function(){
    /// Establish some global variables:
    var out = $('#output');
    var outtext = $('#output_text');
    var wrapper = $('#wrapper');

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
        F_processShot(shotname);
    });
    // Handle event for reset button;
    var resetbutton = $('#reset_button');
    resetbutton.click(function(event){
        event.preventDefault();
        out.slideToggle(100, function(){
            wrapper.center({transition:100})
        });
    });

    var F_processShot = function(shotname){
        var message = "I have converted ";
        message += shotname;
        message += ", have fun!";
        outtext.html(message);
        out.slideToggle(100, function(){
            wrapper.center({transition:100})
        });
        countToAMillion();
    }

    // Hide the output box.
    $('#output').hide();
    // I don't know why I have to do this twice..
    wrapper.center();
    wrapper.center();

    // Center on window resize.
    $(window).bind('resize', function() {
        wrapper.center();
    });

});

