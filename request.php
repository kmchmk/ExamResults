<?php

$file = fopen("config.txt", "r") or die("Unable to open file!");
$servername = trim(fgets($file));
$username = trim(fgets($file));
$password = trim(fgets($file));
$dbname = trim(fgets($file));
fclose($file);


if (isset($_GET["q"])) {
    $index = $_GET["q"];
}
if (isset($_GET["m"])) {
    $method = $_GET["m"];
}
if (isset($_GET["t"])) {
    $table = $_GET['t'];
}
if (isset($_GET["y"])) {
    $year = $_GET['y'];
}




// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
//$conn = new mysqli("localhost", "root", "1234", "exam");
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


if ($method == "getResult") {
    $sql = "SELECT * FROM " . $table . "result WHERE year = '$year' and indexNo = '$index'";
    $result = $conn->query($sql);

    $rows = array();
    $rows[] = 0; //initialize the first element - no of details
    $rows[] = 0; //initialize the second element - no of subjects
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

    while ($r = mysqli_fetch_assoc($result)) {
        //print_r($r);
        foreach ($details as $value) {
            if (isset($r[$value])) {
                $rows[] = $r[$value];
                $rows[0] = $rows[0] + 1;
            }
        }
        if ($table == "gv") {
            if (isset($r['marks'])) {
                $rows[] = "Marks";
                $rows[] = $r['marks'];
                $rows[1] = $rows[1] + 1;
            }
        } else {
            for ($i = 0; $i < 9; $i++) {
                $subject = 'subject' . ($i + 1);
                $mark = 'result' . ($i + 1);
                if (isset($r[$subject]) && isset($r[$mark])) {
                    $rows[] = $r[$subject];
                    $rows[] = $r[$mark];
                    $rows[1] = $rows[1] + 1;
                }
            }
        }
    }

    $json = json_encode($rows);
    echo $json;
}
if ($method == "getYears") {
    $sql = "SELECT DISTINCT year FROM " . $table . "result ORDER BY year";
    $result = $conn->query($sql);
    //$numRows = mysqli_num_rows($result);

    $rows = array();
    while ($r = mysqli_fetch_assoc($result)) {
        $rows[] = $r['year'];
    }

    $json = json_encode($rows);
    echo $json;
}
?>

