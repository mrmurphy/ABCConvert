<div id="history_tabbody" class="tabbody">
    <div id="shotinfo">This is my shot info</div>
    <div class="title">Select a past shot to view here:</div>
    <div id="shotlist">This is my shot list</div>
</div>
<script>
    var UpdateHistoryList = function(callback){
        var selected = $('.histli_active').attr('id');
        $.get("/GetDB/history", function(data){
            $("#shotlist").html(data);
            if (selected !== undefined){
                ActivateHistLi(selected);
            }
            if(callback !== undefined) callback();
        });
    }

    var GetLogById = function(id){
        $.get("/GetDB/history/"+id, function(data){
            $("#shotinfo").html(data);
        });
    }

    var ActivateHistLi = function(num){
        $(".histli_active").removeClass("histli_active");
        $("#"+num).addClass("histli_active");
        GetLogById(num);
    }


    $(document).ready(function() {
        UpdateHistoryList(function(){
            latestid = $(".histli").get(0).id;
            ActivateHistLi(latestid);
        });
    });
</script>
