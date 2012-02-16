<a id="convert_tab" class="tab" href="/convert/"><img src="/images/convert.png"></a>
<a id="history_tab" class="tab" href="/history/"><img src="/images/history.png"></a>
<a id="settings_tab" class="tab" href="/settings/"><img src="/images/settings.png"></a>
<script>
    $(document).ready(function() {
        $('.tab').click(function(e) {
            e.preventDefault();
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
