<?php

$file = fopen("config.txt", "r") or die("Unable to open file!");
$servername = trim(fgets($file));
$username = trim(fgets($file));
$password = trim(fgets($file));
$dbname = trim(fgets($file));
fclose($file);


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}




$method = $_GET['m'];






if ($method == "getResult") {
    $year = "2016";
    $t = $_GET['t'];

    if($t == "Grade 5"){
        $table = "gv";
    }
    else if($t == "O level"){
        $table = "ol";
    }
    else if($t == "A level"){
        $table = "al";
    }
    
    
    
    $index = $_GET['q'];

    $sql = "SELECT * FROM " . $table . "result WHERE year = '$year' and indexNo = '$index'";
    $result = $conn->query($sql);

    $details;
    if ($table == "gv") {
        $details = array("exam", "year", "name", "indexNo", "districtRank");
    }
    if ($table == "ol") {
        $details = array("exam", "year", "name", "indexNo", "syllabus");
    }
    if ($table == "al") {
        $details = array("exam", "year", "name", "indexNo", "districtRank", "islandRank", "zScore", "subjectStream");
    }
    $message = "";
    while ($r = mysqli_fetch_assoc($result)) {
        foreach ($details as $value) {
            if (isset($r[$value])) {
                $message = $message . $value . "-" . $r[$value] . ",\n";
            }
        }
        if ($table == "gv") {
            if (isset($r['marks'])) {
                $message = $message . "Marks" . "-" . $r['marks'] . ",\n";
            }
        } else {
            for ($i = 0; $i < 9; $i++) {
                $subject = 'subject' . ($i + 1);
                $mark = 'result' . ($i + 1);
                if (isset($r[$subject]) && isset($r[$mark])) {
                    $message = $message . $r[$subject] . "-" . $r[$mark] . ",\n";
                }
            }
        }
    }














    $values = new stdClass();
    $values->results = $message;
    $jsonObj = new stdClass();
    $jsonObj->option = "found";
    $jsonObj->values = $values;
    echo json_encode($jsonObj);
}
?>

