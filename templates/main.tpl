<html>
<head>
    <title>ABC Convert</title>
    <link rel="stylesheet/less" type="text/css" href="/styles/main.less">
    <link href='http://fonts.googleapis.com/css?family=Fresca' rel='stylesheet' type='text/css'>
    <script src="/javasc/less.js" type="text/javascript"></script>
    <script src="/javasc/jquery.js"></script>
    <script src="/javasc/splitter.js"></script>
<head>
<body>
    <div id="sidebar">
    %include templates/sidebar
    </div>
    <div id="stage">
    %include
    {{stage()}}
    </div>
    <script>
        /*
        $.get("/GetStage/{{target}}", function(data){
            $("#stage").html(data);
        });
        */
        $('#{{target}}_tab').addClass('tab_active');
    </script>
</body>
</html>
