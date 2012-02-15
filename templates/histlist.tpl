%#<div id="shotsfilter" class="field" contentEditable="true">Filter...</div>
%for entry in ent:
<div class="histli" id="{{entry["ROWID"]}}">
    <span class="entryname">{{entry["name"]}}</span>
</div>
%end
<script>
    $('.histli').click(function(e) {
        e.preventDefault();
        var tid = this.id;
        $.get("/GetDB/history/"+tid, function(data){
            $("#shotinfo").html(data);
        });
        $(".histli_active").removeClass("histli_active");
        $("#"+tid).addClass("histli_active");
    });
    $('.histli:first').click();
</script>
