<!DOCTYPE html>
<?php

$requestURl = "http://localhost/ExamResults/ExamBackEnd/request.php";
$thisPageURL = "http://localhost/ExamResults/Exam/index.php";

$index = "";
$table = "";
$year = "";
if (isset($_GET['q'])) {
    $index = $_GET['q'];
}

if (isset($_GET['t'])) {
    $table = $_GET['t'];
}

if (isset($_GET['y'])) {
    $year = $_GET['y'];
}
?>
<html lang="en" class="gr__torrentz2_eu"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Arrow torrent</title><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="./css/style129.css" type="text/css"><link rel="alternate" type="application/rss+xml" title="Arrow" href="https://torrentz2.eu/feed?f=Arrow"><link rel="search" type="application/opensearchdescription+xml" href="https://torrentz2.eu/opensearch.xml" title="Torrents Search"></head><body data-gr-c-s-loaded="true">
        <div id="wrap">
            <div id="top">
                <h1>
                    <a href="https://torrentz2.eu/" title="Torrents Search">Results<sup>All</sup></a>
                </h1>
                <ul>
                    <li>
                        <a href="https://torrentz2.eu/search" title="Torrent Search">Link1</a>
                    </li>
                    <li>
                        <a href="https://torrentz2.eu/my" title="Personal Search">Link2</a>
                    </li>
                    <li>
                        <a href="https://torrentz2.eu/help" title="Get Help">Link3</a>
                    </li>
                </ul></div>
            <form action="<?php echo $thisPageURL;?>" method="get" class="search" id="search">




                <fieldset id="exams">
                    <select required onchange="javascript:showYears();" name="t" id="category1">
                        <option disabled selected value> -- select an exam -- </option>
                        <option <?php
                        if ($table == "gv") {
                            echo "selected";
                        }
                        ?> value="gv">Grade 5 Scholarship</option>
                        <option <?php
                        if ($table == "ol") {
                            echo "selected";
                        }
                        ?> value="ol">Ordinary Level</option>
                        <option <?php
                        if ($table == "al") {
                            echo "selected";
                        }
                        ?> value="al">Advance Level</option>
                    </select>
                </fieldset>

                <fieldset id="years">
                    <select required name="y" id="category2">
                        <?php
                        if ($year == "") {
                            echo '<option disabled selected value> -- select an year -- </option>';
                        } else {

                            $curl = curl_init();
                            curl_setopt_array($curl, array(
                                CURLOPT_URL => $requestURl."?m=getYears&t=" . $table,
                                CURLOPT_RETURNTRANSFER => true,
                                CURLOPT_ENCODING => "",
                                CURLOPT_MAXREDIRS => 10,
                                CURLOPT_TIMEOUT => 30,
                                CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
                                CURLOPT_CUSTOMREQUEST => "GET",
                                CURLOPT_HTTPHEADER => array(
                                    "cache-control: no-cache"
                                ),
                            ));

                            $response = curl_exec($curl);
                            $result = json_decode($response);
                            $err = curl_error($curl);

                            curl_close($curl);

                            for ($i = 0; $i < count($result); $i++) {
                                $option = '<option ';
                                if ($result[$i] == $year) {
                                    $option = $option . 'selected';
                                }
                                $option = $option . ' value="' . $result[$i] . '">' . $result[$i] . '</option>';

                                echo $option;
                            }
                        }
                        ?>

                        <script>
                            function showYears() {

                                var e = document.getElementById("category1");
                                var exam = e.options[e.selectedIndex].value;
                                var url = "<?php echo $requestURl; ?>"+"?m=getYears&t=" + exam;
                                var xmlHttp = new XMLHttpRequest();
                                xmlHttp.open("GET", url, false);
                                xmlHttp.send();
                                var years = JSON.parse(xmlHttp.responseText);
                                var html = '<option disabled selected value> -- select an year -- </option>';
                                for (var i = 0; i < years.length; i++) {
                                    html += '<option value="' + years[i] + '">' + years[i] + '</option>';
                                }

                                document.getElementById('category2').innerHTML = html;
                            }
                        </script>
                    </select>
                </fieldset>

                <fieldset>
                    <?php
                    echo '<input required type="text" name="q" value="' . $index . '" id="thesearchbox" autocomplete="off">';
                    ?>

                    <ul class="autocomplete" style="top: 119px; left: 84.5px; width: 909px;">
                    </ul>
                    <input type="submit" id="thesearchbutton" value="Search">
                </fieldset>
            </form>
            <div class="SemiAcceptableAds">
                <h3>Details</h3>
                <?php
                $curl = curl_init();
                curl_setopt_array($curl, array(
                    CURLOPT_URL => $requestURl."?m=getResult&t=" . $table . "&y=" . $year . "&q=" . $index,
                    CURLOPT_RETURNTRANSFER => true,
                    CURLOPT_ENCODING => "",
                    CURLOPT_MAXREDIRS => 10,
                    CURLOPT_TIMEOUT => 30,
                    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
                    CURLOPT_CUSTOMREQUEST => "GET",
                    CURLOPT_HTTPHEADER => array(
                        "cache-control: no-cache"
                    ),
                ));

                $response = curl_exec($curl);
                $result = json_decode($response);
                $err = curl_error($curl);

                curl_close($curl);
                if ($table == "gv") {
                    $details = array("Exam", "Year", "Name", "Index No", "District Rank");
                }
                if ($table == "ol") {
                    $details = array("Exam", "Year", "Name", "Index No", "Syllabus");
                }
                if ($table == "al") {
                    $details = array("Exam", "Year", "Name", "Index No", "District Rank", "Island Rank", "Z Score", "Subject Stream");
                }
                for ($i = 0; $i < $result[0]; $i++) {
                    if ($result[$i + 2] != "-") {
                        echo '<dl><dt><strong>' . $details[$i] . '</strong> : ' . $result[$i + 2] . '</dt></dl>';
                    }
                }
                ?>

            </div>
            <div class="SemiAcceptableAds">
                <h3>Results</h3>
            </div>
            <div class="results">

                <h3> <b> Subject </b> » <b> Result </b></h3>
                <?php
                for ($i = 0; $i < $result[1]; $i++) {
                    echo '<dl><dt><font color="blue">' . $result[2 + $result[0] + ($i * 2)] . '</font> » ' . $result[3 + $result[0] + ($i * 2)] . '</dt></dl>';
                }
                ?>
                <p>
                </p>
            </div>

            <div id="recent">This results are not 100% sure and please do not use this website for any kind of formal events.</div>
            <div id="footer"><br></div>

        </div>
    </body>
</html>