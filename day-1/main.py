def add_two(nums):
    for idx, num1 in enumerate(nums):
        for num2 in nums[idx+1:]:
            if (num1 + num2) == 2020:
                return num1 * num2

def add_three(nums):
    for idx, num1 in enumerate(nums):
        for idx1, num2 in enumerate(nums[idx+1:]):
            for num3 in nums[idx1+1:]:
                if (num1 + num2 + num3) == 2020:
                    return num1 * num2 * num3

with open("numbers.txt") as f:
    nums = [int(line) for line in f]

    print("Two numbers\t", add_two(nums))
    print("Three numbers\t", add_three(nums))
