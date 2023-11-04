from typing import List

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    new_list = []
    for i in range(len(nums)):
        #Generator expression care returneaza o serie de 1 pentru fiecare conditie indeplinita, apoi acestea sunt adunate cu sum
        count = sum(1 for num in nums if num < nums[i])
        new_list.append(count)
    return new_list

nums = [10, 4, 9, 8, 9]
print(smallerNumbersThanCurrent(nums))




