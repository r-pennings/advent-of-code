# Format:   L x W x H
# Output:   2*L*W + 2*W*H + 2*H*L

total = 0
with open("input.txt") as _file:
    for line in _file:
        L, W, H = [int(i) for i in line.split('x')]

        sides = [L*W, W*H, H*L]
        area = 2*sides[0] + 2*sides[1] + 2*sides[2]
        slack = min(sides)

        total += (area + slack)

print("Total square feet: ", total)
