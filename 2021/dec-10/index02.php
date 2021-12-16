<?php

$input = file_get_contents("test.txt");

$lines = explode("\r\n", $input);

function close($left, $right): bool
{
    return ($left === "(" && $right === ")") ||
        ($left === "[" && $right === "]") ||
        ($left === "{" && $right === "}") ||
        ($left === "<" && $right === ">");
}

function getCorrupted($line)
{
    $result = null;
    $stack = [];

    $chars = str_split($line);
    foreach ($chars as $char) {
        if (in_array($char, ["(", "[", "{", "<"])) {
            $stack[] = $char;
            continue;
        }

        if (close($stack[count($stack) - 1], $char)) {
            array_pop($stack);
            continue;
        }

        $result = $char;
        break;
    }

    return $result;
}

$characters = [
    ")" => 0,
    "]" => 0,
    "}" => 0,
    ">" => 0
];

function filter($array, $character): array
{
    return array_filter($array, fn($c) => $c === $character);
}

$sum = 0;
foreach ($lines as $line) {
    // Check if line is corrupted
    $corrupted = getCorrupted($line);

    if ($corrupted !== null) {
        // If line is corrupted check what is needed to close every tag
        $characters[")"] = count(filter(str_split($line), "(")) - count(filter(str_split($line), ")"));
        $characters["]"] = count(filter(str_split($line), "[")) - count(filter(str_split($line), "]"));
        $characters["}"] = count(filter(str_split($line), "{")) - count(filter(str_split($line), "}"));
        $characters[">"] = count(filter(str_split($line), "<")) - count(filter(str_split($line), ">"));
    }
}

var_dump($characters);

// Translate
$elements = [
    ")" => 1,
    "]" => 2,
    "}" => 3,
    ">" => 4
];

$result = [0];
//$result = array_map(fn($char) => $elements[$char], $characters);
echo "PART 2: ".array_sum($result);