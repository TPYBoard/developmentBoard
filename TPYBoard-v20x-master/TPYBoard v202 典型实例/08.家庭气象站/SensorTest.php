<?php
    $time_="获取时间:".date('Y-m-d H:i:s');
    $data_="传感器数据:Sensor Error!";
    $state_="No";
    if(is_array($_GET)&&count($_GET)>1)
    { 
        $data_="";
        //获取温度
        if(isset($_GET["t"]))
        { 
            $para=$_GET["t"];
            $data_.="传感器数据:温度:".$para." ℃ - ";
        }
        //获取湿度
        if(isset($_GET["h"]))
        { 
            $para=$_GET["h"];
            $data_.="湿度:".$para." % ";
            $state_="Yes";
        }   
    }
    $myfile = fopen("sensor.txt", "w");
    $txt = $time_."<br /><br />".$data_;
    fwrite($myfile, $txt);
    fclose($myfile);
    echo $state_;
?>