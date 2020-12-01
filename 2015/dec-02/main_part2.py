# Format:   L x W x H
# Output:   L + L + W + W + L x W x H

total = 0
with open("input.txt") as _file:
    for line in _file:
        L, W, H = [int(i) for i in line.split('x')]

        ribbon = 2 * min(L+W, W+H, H+L)
        bow = L * W * H

        total += (ribbon + bow)

print("Total feet: ", total)