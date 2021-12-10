<?php

$input = file_get_contents("input.txt");

$lines = explode("\r\n", $input);

$entries = array();
foreach ($lines as $line) {
    [$input, $output] = explode(" | ", $line);
    $input = explode(" ", $input);
    $output = explode(" ", $output);
    $entries[] = ["in" => $input, "out" => $output];
}

// PART 1
$uniques = [2 => 0, 3 => 0, 4 => 0, 7 => 0];
foreach ($entries as $entry) {
    foreach ($entry["out"] as $e) {
        if (isset($uniques[strlen($e)])) {
            $uniques[strlen($e)]++;
        }
    }
}

echo "PART 1: ".array_sum($uniques);

// PART 2
foreach ($entries as $entry) {
    usort($entry["in"], function ($a, $b) {
        if ($a == $b) return 0;
        return strlen($a) < strlen($b) ? -1 : 1;
    });
}