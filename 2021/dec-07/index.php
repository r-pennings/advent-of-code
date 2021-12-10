<?php

$input = file_get_contents("input.txt");
$inputArray = explode(",", $input);

$positions = count($inputArray);

// PART 1
$cheapest = null;
foreach (range(1, $positions) as $pos) {
    $fuelUsed = 0;
    foreach ($inputArray as $item) {
        $fuelUsed += ($item > $pos) ? ($item - $pos) : ($pos - $item);
    }

    if ($cheapest === null || $fuelUsed < $cheapest) {
        $cheapest = $fuelUsed;
    }
}

echo "PART 1: ".$cheapest;

// PART 2
$cheapest = null;
foreach (range(1, $positions) as $pos) {
    $fuelUsed = 0;
    foreach ($inputArray as $item) {
        $steps = 0;
        if ($item > $pos) {
            $steps = $item - $pos;
        } else if ($item < $pos) {
            $steps = $pos - $item;
        }

        if ($steps > 0) {
            $fuel = 0;
            foreach (range(1, $steps) as $step) {
                $fuel += $step;
            }

            $fuelUsed += $fuel;
        }
    }

    if ($cheapest === null || $fuelUsed < $cheapest) {
        $cheapest = $fuelUsed;
    }
}

echo "PART 2: ".$cheapest;