from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    i = 0
    j = 0
    new_list = []
    count = 0
    if all(element == nums[i] for element in nums):
        new_list = [0] * len(nums)
        return new_list
    while i <= len(nums)-1:
        if j > len(nums) - 1:
            new_list.append(count)
            if nums[i] == nums[-1]:
                return new_list
            j = 0
            i += 1
            count=0
        if nums[i] > nums[j]:
            count += 1
        j += 1
    return new_list

nums = [10,4,9,8,9]
print(smallerNumbersThanCurrent(nums))