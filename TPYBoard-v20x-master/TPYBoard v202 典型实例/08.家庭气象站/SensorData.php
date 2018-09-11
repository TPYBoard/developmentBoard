<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>温湿度传感器实验</title>
<script type="text/javascript">
    var t;
    var te_html_str="N/A";
    function timedCount()
    {
      <?php
            
        $myfile = fopen("sensor.txt", "r");
        $txt =fread($myfile,filesize("sensor.txt"));
        fclose($myfile);
        if($txt!="")
        {
            echo "te_html_str='".$txt."';";
        }
        ?>
      document.getElementById('test').innerHTML=te_html_str;
      t=setTimeout("javascript:location=location;",1000)
    }
</script>
</head>
  <body onload="timedCount()">
  
  <center>
  <div style="margin-top:80px">
    <h2>TPYBoardV202_温湿度传感器实验</h2>
    <div id="test"></div>
  </div>
   </center>

</body>
</html>