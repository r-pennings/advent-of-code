<?php

$input = file_get_contents("input.txt");
$lines = explode("\r\n", $input);

function most($items): string
{
    return (string)($items[0] !== $items[1] ? array_search(max($items), $items) : 1);
}

function least($items): string
{
    return (string)($items[0] !== $items[1] ? array_search(min($items), $items) : 0);
}

function filter($items, $index, $filter): array
{
    return array_filter($items, fn($item) => $item[$index] === (string)$filter);
}

function count_by_index($items, $index): array
{
    return array_count_values(array_map(fn($line) => $line[$index], $items));
}

// PART 1
$gamma_rate = $epsilon_rate = null;

foreach (range(0, strlen($lines[0]) - 1) as $index) {
    $items = count_by_index($lines, $index);
    $gamma_rate .= most($items);
    $epsilon_rate .= least($items);
}

$power_consumption = (float)(bindec($gamma_rate) * bindec($epsilon_rate));

echo "PART 1: " . $power_consumption;

// PART 2
$gamma_rate = $epsilon_rate = null;

$items = $lines;
$index = 0;
while (count($items) > 1) {
    $tmp = count_by_index($items, $index);
    $items = filter($items, $index, most($tmp));

    $index++;
}

$gamma_rate = array_values($items)[0];

$items = $lines;
$index = 0;
while (count($items) > 1) {
    $tmp = count_by_index($items, $index);
    $items = filter($items, $index, least($tmp));

    $index++;
}

$epsilon_rate = array_values($items)[0];

$power_consumption = (float)(bindec($gamma_rate) * bindec($epsilon_rate));

echo "PART 2: " . $power_consumption;