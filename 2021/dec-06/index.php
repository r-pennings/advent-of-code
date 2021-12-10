<?php

$input = file_get_contents("input.txt");

$inputArray = explode(",", $input);

function grow(&$schoolArray)
{
    $tmpZero = $schoolArray[0];

    for ($i = 0; $i < 8; $i++) {
        $schoolArray[$i] = $schoolArray[$i + 1];
    }

    $schoolArray[8] = $tmpZero;
    $schoolArray[6] += $tmpZero;
}

function numberAfterDays($schoolArray, $days)
{
    $schoolArrayCopy = [...$schoolArray];

    for ($i = 0; $i < $days; $i++) {
        grow($schoolArrayCopy);
    }

    return array_sum($schoolArrayCopy);
}

$lanternFishArray = [];
for ($i = 0; $i < 9; $i++) {
    $lanternFishArray[$i] = 0;
}

foreach ($inputArray as $i) {
    $lanternFishArray[$i]++;
}

echo "PART 1: ".numberAfterDays($lanternFishArray, 80);

echo "PART 2: ".numberAfterDays($lanternFishArray, 256);