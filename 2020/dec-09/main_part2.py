def calc_number(nums, preamble):
    for index in range(preamble, len(nums)):
        stack = nums[index - preamble:index]
        num = nums[index]
        has_sum = False
        for i in stack:
            for j in stack[1:]:
                if i + j == num:
                    has_sum = True

        if not has_sum:
            return num


def calc_weakness(nums, invalid_num):
    for i in range(0, len(nums) - 1):
        for j in range(1, len(nums) - 1):
            stack = nums[i:j]
            if len(stack) >= 2 and sum(stack) == invalid_num:
                print("min", min(stack), "max", max(stack))
                return min(stack) + max(stack)


nums = [int(num.strip()) for num in open("input.txt")]

print("weakness", calc_weakness(nums, calc_number(nums, 25)))
