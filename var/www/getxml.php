<?php

/* http://www.transitchicago.com/developers/traintrackerapply.aspx */
$apiKey = "YOUR_API_KEY_HERE";
/* should just be the bus number */
$busRoute = "YOUR_ROUTE_NUMBER_HERE";
/* http://www.transitchicago.com/riding_cta/how_to_guides/bustrackerlookup_stoplists.aspx */
$stopID = "YOUR_STOP_ID_HERE";

$url = 'http://www.ctabustracker.com/bustime/api/v1/getpredictions?key=' .$apiKey. '&top=2&rt=' .$busRoute. '&stpid=' .$stopID;

$xml = simplexml_load_file($url);
echo $xml->asXML();

?>