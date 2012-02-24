<script>
    $('#convert').addClass('.tab_active');
</script>
<div id="convert_tabbody" class="tabbody">
<div class="shot">
    <div id="convert_seldiv">
        <span class="title">Where's the file to convert?</span>
        <div id="convert_shotfield" tabindex="1" class="field" contentEditable='true'>{{filepath}}</div>
        <!--<div class="filepicker">This is where the file picker will be.</div>--!>
        <div class="button" tabindex="1" id="startconvert">Go!</div>
    </div>
    <div id="convert_progdiv">
        <div class="textview" id="logview">Log.</div>
        <div id="progressbar"><span id='progpercent_wrap'><span id='progpercent'>50</span>%</span></div>
        <div class="button" tabindex="1" id="newconvert">Do another one!</div>
    </div>
</div>
</div>
<script>
    // Global variables:
    var currentid;
    // Define functions.
    function MonitorProgress(tid, dispdivid){
        $.get("/GetDB/single/progress/"+tid, function(prog){
            $.get("/GetDB/single/log/"+tid, function(log){
                if (log === ""){
                    log = "Maya is starting..."
                }
                $("#"+dispdivid).html(log);
            });
            $("#progressbar").progressbar({
                value: parseInt(prog)
            });
            $("#progpercent").html(prog);
            if(prog === '100'){
                convert_finishstate();
                return;   
            }
            setTimeout(MonitorProgress, 250, tid, dispdivid);
        });
    }

    function convert_seldivstate(){
        $("#convert_progdiv").hide();
        $("#convert_seldiv").show();
    }
    function convert_progdivstate(){
        $("#convert_progdiv").slideDown();
        $("#progressbar").slideDown();
        $("#convert_seldiv").slideUp();
        $("#newconvert").slideUp();
    }
    function convert_finishstate(){
        $("#convert_progdiv").slideDown();
        $("#progressbar").slideUp();
        $("#convert_seldiv").fadeOut();
        $("#newconvert").slideDown();
    }
    convert_seldivstate();


    $("#startconvert").click(function(){
        var convpath = $('#convert_shotfield').text();
        $.get("/RunConvert/"+convpath, function(data){
            // Do some error checking:
            if (data.substring(0, 5) == 'ERROR'){
                $("#logview").html(data);
                convert_finishstate();
                return;
            }
            currentid = data;    
            MonitorProgress(currentid, "logview");
        });
        convert_progdivstate();
    });
    $("#convert_progbar").click(function(){
        convert_finishstate();
    });
    $("#newconvert").click(function(){
        convert_seldivstate();
    });
    $("#convert_shotfield").keypress(function(event){
        if( event.which == 13 ){
            event.preventDefault();
            $("#startconvert").focus();
        }
    });
    $(".button").keypress(function(event){
        if( event.which == 13 ){
            event.preventDefault();
            $("#"+this.id).click();
        }
    });
</script>
