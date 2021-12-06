<?php

$input = file_get_contents("input.txt");
$lines = explode("\r\n", $input);

// PART 1
$x = $y = 0;
foreach ($lines as $line) {
    [$direction, $steps] = explode(" ", $line);

    if ($direction === "forward") {
        $x += $steps;
    }

    if ($direction === "up") {
        $y -= $steps;
    }

    if ($direction === "down") {
        $y += $steps;
    }
}

echo "PART 1: " . ($x * $y);

// PART 2
$x = $y = $aim = 0;
foreach ($lines as $line) {
    [$direction, $steps] = explode(" ", $line);

    if ($direction === "forward") {
        $x += $steps;
        $y += ($aim * $steps);
    }

    if ($direction === "up") {
        $aim -= $steps;
    }

    if ($direction === "down") {
        $aim += $steps;
    }
}

echo "PART 2: " . ($x * $y);