<a id="convert_tab" class="tab" href="/GetStage/convert"><img src="/images/convert.png"></a>
<a id="history_tab" class="tab" href="/GetStage/history"><img src="/images/history.png"></a>
<a id="settings_tab" class="tab" href="/GetStage/settings"><img src="/images/settings.png"></a>
<script>
    $(document).ready(function() {
        $('.tab').click(function(e) {
            event.preventDefault();
            var linker = this.href;
            var tid = this.id;
            $.get(linker, function(data){
                $("#stage").html(data);
            });
            $(".tab_active").removeClass("tab_active");
            $("#"+tid).addClass("tab_active");
        });
    });
</script>
