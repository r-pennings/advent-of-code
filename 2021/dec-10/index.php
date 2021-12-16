<?php

$input = file_get_contents("input.txt");

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

$characters = [];
foreach ($lines as $line) {
    $corrupted = getCorrupted($line);
    if ($corrupted !== null) {
        $characters[] = $corrupted;
    }
}

// Translate
$elements = [
    ")" => 3,
    "]" => 57,
    "}" => 1197,
    ">" => 25137
];

$result = array_map(fn($char) => $elements[$char], $characters);
echo "PART 1: ".array_sum($result);