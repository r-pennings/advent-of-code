<?php

$input = file_get_contents("input.txt");

$lines = explode("\r\n", $input);

$map = [];
foreach ($lines as $line) {
    $map[] = str_split($line);
}

function getAdjacent($map, $x, $y): array
{
    $adjacent = [];
    // Left
    if ($x > 0 && isset($map[$y][$x - 1])) {
        $adjacent[] = $map[$y][$x - 1];
    }
    // Up
    if ($y > 0 && isset($map[$y - 1][$x])) {
        $adjacent[] = $map[$y - 1][$x];
    }
    // Right
    if ($x < count($map[$y]) - 1 && isset($map[$y][$x + 1])) {
        $adjacent[] = $map[$y][$x + 1];
    }
    // Down
    if ($y < count($map) - 1 && isset($map[$y + 1][$x])) {
        $adjacent[] = $map[$y + 1][$x];
    }

    return $adjacent;
}

$points = [];
for ($y = 0; $y < count($map); $y++) {
    for ($x = 0; $x < count($map[$y]); $x++) {
        $current = $map[$y][$x];

        foreach (getAdjacent($map, $x, $y) as $value) {
            if ($value <= $current) {
                continue 2;
            }
        }

        $points[] = (int)$current;
    }
}

echo "PART 1: ".(array_sum($points) + count($points));
