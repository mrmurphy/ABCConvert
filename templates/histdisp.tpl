%# Here I had to split the log by \n because I don't know how to get bottle
%# to render html from the characters in the dictionary.
<div class="histtitle">
Shot name:<span class='titlebody'> {{ent['name']}}<br></span>
When:<span class='titlebody'> {{ent['date']}}<br></span>
Progress:<span class='titlebody'> {{ent['progress']}}</span>
</div>
<div class="histlog">
%lines = ent['log'].split('<br>')
%for line in lines:
<p>{{line}}</p>
%end
</div>
