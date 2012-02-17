<a id="convert_tab" class="tab"><img src="/static/images/convert.png"></a>
<a id="history_tab" class="tab"><img src="/static/images/history.png"></a>
%#<a id="settings_tab" class="tab"><img src="/static/images/settings.png"></a>
<script>

    var SwitchToTab = function(whichtab){
        $(".tabbody").hide();
        $(".tab_active").removeClass("tab_active");
        $("#"+whichtab+"body").show();
        $("#"+whichtab).addClass("tab_active");
    }

    $(document).ready(function() {

        $('.tab').click(function(e) {
            e.preventDefault();
            var tid = this.id;
            SwitchToTab(tid);
        });

        $("#history_tab").click(function(e) {
            UpdateHistoryList();
        });

    });
</script>
