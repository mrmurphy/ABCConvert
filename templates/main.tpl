<html>
<head>
    <title>ABC Convert</title>
    <link rel="stylesheet/less" type="text/css" href="/styles/main.less">
    <script src="/javasc/less.js" type="text/javascript"></script>
    <script src="/javasc/jquery.js"></script>
    <script src="/javasc/splitter.js"></script>
<head>
<body>
    <div id="sidebar">
    %include templates/sidebar
    </div>
    <div id="stage">This stage will contain the page for </div>
    <script>
        $.get("/GetStage/{{target}}", function(data){
            $("#stage").html(data);
        });
        $('#{{target}}_tab').addClass('tab_active');
    </script>
</body>
</html>
