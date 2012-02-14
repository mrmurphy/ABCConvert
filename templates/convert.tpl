%setdefault('filepath', '/grp5/estefan/production3d/scenes/shots/')
%def stage():
<script>
    $('#convert').addClass('.tab_active');
</script>
<div id="convertwrapper">
<div class="shot">
    <div id="convert_seldiv">
        <span class="title">Where's the file to convert?</span>
        <div class="field" contentEditable='true'>{{filepath}}</div>
        <!--<div class="filepicker">This is where the file picker will be.</div>--!>
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
        $("#convert_progdiv").slideDown();
        $("#convert_progbar").slideDown();
        $("#convert_seldiv").slideUp();
        $("#newconvert").slideUp();
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
%return ""
%end
%rebase templates/main stage=stage, target="convert"
