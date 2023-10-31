from typing import List
"""I began by creating a for loop to iterate through the nums list.

1. Skipped the first element of the list since, regardless of its value, it would be added to its sum with 0.
2. Replaced nums[i] with the sum of itself and the previous value, i.e., nums[i-1].
3. Finally, returned the new nums list."""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums