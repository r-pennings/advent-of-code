EMPTY = 'L'
OCCUPIED = '#'

with open("input.txt") as f:
    lines = [list(line) for line in [line.rstrip() for line in f.readlines()]]

rows, cols = len(lines), len(lines[0])
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_occupied(row, col, lines):
    count = 0
    for i, j in deltas:
        xi, xj = row + i, col + j

        if 0 <= xi < rows and 0 <= xj < cols and lines[xi][xj] == OCCUPIED:
            count += 1
    return count


def check_occupied(lines, thresh=4):
    while True:
        valid = True
        tmp_lines = [r.copy() for r in lines]

        for i, r in enumerate(tmp_lines):
            for j, c in enumerate(r):
                count = count_occupied(i, j, tmp_lines)

                if count == 0 and c == EMPTY:
                    lines[i][j] = OCCUPIED
                elif count >= thresh and c == OCCUPIED:
                    lines[i][j] = EMPTY
                valid &= (r[j] == lines[i][j])
        if valid:
            break

    answer = 0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == OCCUPIED:
                answer += 1

    print("seats:", answer)


check_occupied(lines)
