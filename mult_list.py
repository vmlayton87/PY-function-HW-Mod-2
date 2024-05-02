# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] * mult_list(nums[1:])

print(mult_list([1,2]))
print(mult_list([1,2,5,10]))
print(mult_list([1,-2]))
print(mult_list([1,-2, 0.125]))