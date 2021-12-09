<?php

ini_set('memory_limit', '-1');

$input = file_get_contents("test.txt");

$inputArray = explode(",", $input);

function handle($inputArray, $maxDays): int
{
    $fishPerAge = array();

    foreach ($inputArray as $item) {
        $fishPerAge[] = $item;
    }

    for ($day = 0; $day < $maxDays; $day++) {
        $fishPerAgePerDay = array();

        // Update array
        foreach (range(0, count($array) - 1) as $x) {
            $array[$x]--;

            if ($array[$x] < 0) {
                $array[$x] = 6;
                $array[] = 8;
            }
        }
    }

    return count($array);
}

var_dump(microtime(true));
echo "PART 1: ".handle($inputArray, 80).PHP_EOL;
var_dump(microtime(true));

var_dump(microtime(true));
echo "PART 2: ".handle($inputArray, 200).PHP_EOL;
var_dump(microtime(true));
//echo PHP_EOL.PHP_EOL;
//echo PHP_EOL."PART 2: ".handle($inputArray, 256);
