<link href='http://fonts.googleapis.com/css?family=Terminal+Dosis' rel='stylesheet' type='text/css'>
%for entry in ent:
<div class="histli" id="{{entry["ROWID"]}}">
    <span class="entryname">{{entry["name"]}}</span>
</div>
%end
<script>
    $(document).ready(function() {
        $('.histli').click(function(e) {
            event.preventDefault();
            var tid = this.id;
            $.get("/GetDB/history/"+tid, function(data){
                $("#shotinfo").html(data);
            });
            $(".histli_active").removeClass("histli_active");
            $("#"+tid).addClass("histli_active");
        });
    });
</script>
