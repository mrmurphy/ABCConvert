<div id="historywrapper">
    <div id="shotinfo">This is my shot info</div>
    <div id="shotlist">This is my shot list</div>
</div>
<script>
    $(document).ready(function() {
        $.get("/GetDB/history", function(data){
            $("#shotlist").html(data);
        });
    });
</script>
