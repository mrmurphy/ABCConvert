%#<ul id="shotsfilter" class="field" contentEditable="true">Filter...</div>
%ent.reverse()
%for entry in ent:
<div class="histli" id="{{entry["ROWID"]}}">
    <span class="entryname">{{entry["name"]}}</span>
    : {{entry['date']}} : {{entry['progress']}}%
</div>
%end
<script>
    $('.histli').click(function(e) {
        e.preventDefault();
        var tid = this.id;
        ActivateHistLi(tid);
    });
    //$('.histli:first').click();
</script>
