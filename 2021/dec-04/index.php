<?php

$input = file_get_contents("input.txt");

$input = trim($input);
$input = str_replace("\r\n", " ", $input);
$input = preg_replace("!\s+!", " ", $input);
$inputArray = explode(" ", $input);

$balls = array_shift($inputArray);
$balls = explode(",", $balls);

$cards = array_chunk($inputArray, 25);

// Functions
function calculateWinner($markedCard, $gameArray): int
{
    $cardSum = 0;
    foreach ($gameArray[$markedCard]["rows"] as $row) {
        $cardSum += (int)array_sum($row);
    }
    return $cardSum;
}

function createGame($cards, $cardNr): array
{
    $game = array();

    $cols = array();
    foreach ($cards as $card) {
        $rows = array_chunk($card, 5);

        for ($y = 0; $y < 5; $y++) {
            for ($x = 0; $x < 5; $x++) {
                $cols[$y][$x] = $card[($y + ($x * 5))];
            }
        }

        $game[$cardNr]["rows"] = $rows;
        $game[$cardNr]["cols"] = $cols;
        $cardNr++;
    }

    return $game;
}

// PART 1
$winners = array();
$cardNr = 0;
$game = createGame($cards, $cardNr);

$ballIndex = 0;
$result = null;
while (!$result) {
    $ball = $balls[$ballIndex];

    $cardNr = 0;
    foreach ($game as $card) {
        if (!in_array($cardNr, $winners)) {
            $rowNum = $colNum = 0;

            // check rows
            foreach ($card["rows"] as $row) {
                $found = array_search($ball, $row);
                if ($found !== false) {
                    $cellsFound = count($game[$cardNr]["rows"][$rowNum]);
                    unset($game[$cardNr]["rows"][$rowNum][$found]);
                    $cellsLeft = count($game[$cardNr]["rows"][$rowNum]);

                    if (!$cellsLeft) {
                        $result = calculateWinner($cardNr, $game) * $ball;
                        break;
                    }
                }
                $rowNum++;
            }

            // check cols
            foreach ($card["cols"] as $col) {
                $found = array_search($ball, $col);
                if ($found !== false) {
                    $cellsFound = count($game[$cardNr]["cols"][$colNum]);
                    unset($game[$cardNr]["cols"][$colNum][$found]);
                    $cellsLeft = count($game[$cardNr]["cols"][$colNum]);
                    if (!$cellsLeft) {
                        $result = calculateWinner($cardNr, $game) * $ball;
                        break;
                    }
                }
                $colNum++;
            }
        }
        $cardNr++;
    }

    $ballIndex++;
}

echo "PART 1: ".$result;

// PART 2
$winners = array();
$cardNr = 0;
$game = createGame($cards, $cardNr);

$result = null;
foreach ($balls as $ball) {
    $cardNr = 0;
    foreach ($game as $card) {
        if (!in_array($cardNr, $winners)) {
            $rowNum = $colNum = 0;

            // check rows
            foreach ($card["rows"] as $row) {
                $found = array_search($ball, $row);
                if ($found !== false) {
                    $cellsFound = count($game[$cardNr]["rows"][$rowNum]);
                    unset($game[$cardNr]["rows"][$rowNum][$found]);
                    $cellsLeft = count($game[$cardNr]["rows"][$rowNum]);

                    if (!$cellsLeft) {
                        $result = calculateWinner($cardNr, $game) * $ball;
                        $winners[] = $cardNr;
                    }
                }
                $rowNum++;
            }

            // check cols
            foreach ($card["cols"] as $col) {
                $found = array_search($ball, $col);
                if ($found !== false) {
                    $cellsFound = count($game[$cardNr]["cols"][$colNum]);
                    unset($game[$cardNr]["cols"][$colNum][$found]);
                    $cellsLeft = count($game[$cardNr]["cols"][$colNum]);
                    if (!$cellsLeft) {
                        $result = calculateWinner($cardNr, $game) * $ball;
                        $winners[] = $cardNr;
                    }
                }
                $colNum++;
            }
        }
        $cardNr++;
    }
}

echo "PART 2: ".$result;