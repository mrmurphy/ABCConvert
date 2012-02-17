<html>
<head>
    <title>ABC Convert</title>
    <link rel="stylesheet/less" type="text/css" href="/static/styles/main.less">
    <link href='http://fonts.googleapis.com/css?family=Fresca' rel='stylesheet' type='text/css'>
    <script src="/static/javasc/less.js" type="text/javascript"></script>
    <script src="/static/javasc/jquery.js"></script>
<head>
<body>
    <div id="sidebar">
    %include templates/sidebar
    </div>
    <div id="stage">
        %include templates/convert filepath=filepath
        %include templates/history
        %include templates/settings
    </div>
    <script>
        SwitchToTab('{{active}}_tab');
    </script>
</body>
</html>
