<?php

$input = file_get_contents("test.txt");
$lines = explode("\r\n", $input);

// PART 1
$tmp = $lines;
$balls = array_shift($tmp);
$balls = explode(",", $balls);

array_shift($tmp); // empty line

$boards = [];
$index = 0;
foreach ($tmp as $line) {
    $i = "board-" . $index;

    $boards[$i] = [];

    // Rows
    $boards[$i]["rows"] = [];

    if (!empty($line)) {
        preg_match_all("/(\d+) *?(\d+) *?(\d+) *?(\d+) *?(\d+)/", $line, $matches);

        $array = [];
        foreach (range(1, count($matches) - 1) as $idx) {
            $array[] = $matches[$idx][0];
        }

        $boards[$i]["rows"][] = $array;
    } else {
        $index++;
    }

    // Cols
    $boards[$i]["cols"] = [];
}

var_dump($boards);

//$boards

echo "PART 1: ?";

// PART 2

echo "PART 2: ?";