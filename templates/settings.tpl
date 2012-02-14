%def stage():
<div id="settings_wrapper">
<div id="settings_outline">
<span class="title">Base path for shots:</span><div class="field" contentEditable="true">/</div>
<div class="button" id="settings_but_save">Save</div>
</div>
</div>
%return ""
%end
%rebase templates/main stage=stage, target="settings"
