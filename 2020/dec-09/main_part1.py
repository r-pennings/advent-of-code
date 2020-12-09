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

nums = [int(num.strip()) for num in open("input.txt")]

print("wrong number", calc_number(nums, 25))