%def stage():
<div id="historywrapper">
    <div id="shotinfo">This is my shot info</div>
    <div id="shotlist">This is my shot list</div>
</div>
<script>
    //$('#historysplitter').splitter({sizeRight: true});
    $.get("/GetDB/history", function(data){
        $("#shotlist").html(data);
    });
</script>
%return ""
%end
%rebase templates/main stage=stage, target="history"
