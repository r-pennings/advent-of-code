<?php

$input = file_get_contents("input.txt");
$lines = explode("\r\n", $input);

function compare($prev, $curr): bool
{
    return $prev !== 0 && $curr > $prev;
}

// PART 1
$previous = $increased = 0;

foreach ($lines as $line) {
    if (compare($previous, $line)) {
        $increased++;
    }

    $previous = (int)$line;
}

echo "PART 1: " . $increased;

// PART 2
$previous = $increased = 0;

for ($i = 0; $i < count($lines) - 2; $i++) {
    $sum = $lines[$i] + $lines[$i + 1] + $lines[$i + 2];

    if (compare($previous, $sum)) {
        $increased++;
    }

    $previous = (int)$sum;
}

echo "PART 2: " . $increased;
