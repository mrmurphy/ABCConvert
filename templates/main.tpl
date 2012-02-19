<html>
<head>
    <title>ABC Convert</title>
    <link type="text/css" href="/static/styles/css/custom-theme/jquery-ui-1.8.17.custom.css" rel="stylesheet" />	
    <link rel="stylesheet/less" type="text/css" href="/static/styles/main.less">
    <link href='http://fonts.googleapis.com/css?family=Fresca' rel='stylesheet' type='text/css'>
    <script src="/static/javasc/less.js" type="text/javascript"></script>
    <script src="/static/javasc/jquery.js"></script>
    <script src="/static/javasc/jquery-ui-1.8.17.custom.min.js"></script>
<head>
<body>
    <div id="sidebar">
    %include templates/sidebar
    </div>
    <div id="stage">
        %include templates/convert filepath=filepath
        %include templates/history
    </div>
    <script>
        SwitchToTab('{{active}}_tab');
    </script>
</body>
</html>
