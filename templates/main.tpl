<html>
<head>
    <title>ABC Convert</title>
    <link rel="stylesheet/less" type="text/css" href="/styles/main.less">
    <link href='http://fonts.googleapis.com/css?family=Fresca' rel='stylesheet' type='text/css'>
    <script src="/javasc/less.js" type="text/javascript"></script>
    <script src="/javasc/jquery.js"></script>
<head>
<body>
    <div id="sidebar">
    %include templates/sidebar
    </div>
    <div id="stage">
        %include templates/convert
        %include templates/history
        %include templates/settings
    </div>
    <script>
        $('#{{active}}_tab').addClass('tab_active');
    </script>
</body>
</html>
