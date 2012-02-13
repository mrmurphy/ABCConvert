<script>
    $('#convert').addClass('.tab_active');
</script>
<div id="convertwrapper">
<div class="shot">
    <div id="convert_seldiv">
        <span class="title">Select File to Convert:</span>
        <div class="filepicker">This is where the file picker will be.</div>
        <div class="button" id="startconvert">Go!</div>
    </div>
    <div id="convert_progdiv">
        <div class="textview" id="logview">This is where log things will show up.</div>
        <div class="progressbar" id="convert_progbar">I'm a progress bar.</div>
        <div class="button" id="newconvert">Do another one!</div>
    </div>
</div>
</div>
<script>
    function convert_seldivstate(){
        $("#convert_progdiv").hide();
        $("#convert_seldiv").show();
    }
    function convert_progdivstate(){
        $("#convert_progdiv").show();
        $("#convert_progbar").show();
        $("#convert_seldiv").hide();
        $("#newconvert").hide();
    }
    function convert_finishstate(){
        $("#convert_progdiv").slideDown();
        $("#convert_progbar").slideUp();
        $("#convert_seldiv").fadeOut();
        $("#newconvert").slideDown();
    }
    convert_seldivstate();

    $("#startconvert").click(function(){
        convert_progdivstate();
    });
    $("#convert_progbar").click(function(){
        convert_finishstate();
    });
    $("#newconvert").click(function(){
        convert_seldivstate();
    });
</script>
