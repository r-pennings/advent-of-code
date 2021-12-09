<?php

function size($lines): array
{
    $width = $height = 0;

    foreach ($lines as $line) {
        [$start, $end] = explode(" -> ", $line);

        [$x1, $y1] = explode(",", $start);
        [$x2, $y2] = explode(",", $end);

        if ($x1 > $width) {
            $width = $x1;
        }

        if ($x2 > $width) {
            $width = $x2;
        }

        if ($y1 > $height) {
            $height = $y1;
        }

        if ($y2 > $height) {
            $height = $y2;
        }
    }

    return [$width, $height];
}

function grid($width, $height): array
{
    $grid = [];
    for ($y = 0; $y <= $height; $y++) {
        $grid[$y] = [];

        for ($x = 0; $x <= $width; $x++) {
            $grid[$y][$x] = 0;
        }
    }
    return $grid;
}

function handle($diagonal = false): int
{
    $input = file_get_contents("input.txt");
    $lines = explode("\r\n", $input);

    [$width, $height] = size($lines);

    $grid = grid($width, $height);

    foreach ($lines as $line) {
        [$start, $end] = explode(" -> ", $line);
        [$x1, $y1] = explode(",", $start);
        [$x2, $y2] = explode(",", $end);

        if ($x1 === $x2) {
            foreach (range($y1, $y2) as $y) {
                $grid[$y][$x1]++;
            }
        } else if ($y1 === $y2) {
            foreach (range($x1, $x2) as $x) {
                $grid[$y1][$x]++;
            }
        } else if ($diagonal) {
            if ($y2 > $y1 && $x2 > $x1) { // up -> down && left -> right
                foreach (range(0, $y2 - $y1) as $c) {
                    $grid[$y1 + $c][$x1 + $c]++;
                }
            } elseif ($y2 > $y1 && $x2 < $x1) { // up -> down && right -> left
                foreach (range(0, $y2 - $y1) as $c) {
                    $grid[$y1 + $c][$x1 - $c]++;
                }
            } elseif ($y2 < $y1 && $x2 > $x1) { // down -> up && left -> right
                foreach (range(0, $y1 - $y2) as $c) {
                    $grid[$y1 - $c][$x1 + $c]++;
                }
            } elseif ($y2 < $y1 && $x2 < $x1) { // down -> up && right -> left
                foreach (range(0, $y1 - $y2) as $c) {
                    $grid[$y1 - $c][$x1 - $c]++;
                }
            }
        }
    }

    $counter = 0;
    for ($y = 0; $y < count($grid); $y++) {
        for ($x = 0; $x < count($grid[$y]); $x++) {
            if ($grid[$y][$x] >= 2) {
                $counter++;
            }
        }
    }

    return $counter;
}

echo "PART 1: ".handle(false);
echo "PART 2: ".handle(true);