from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_val = max(candies)
        bool_list = []
        for i in range(n):
            if candies[i]+extraCandies >= max_val:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
"""
For this problem, I initialized the variable n = the number of elements in the 'candies' list, 
max_val = the maximum value in the 'candies' list, and bool_list = an empty list where we will put all the boolean values.

1. For loop in the range of the number of elements in the list.
2. If the value added to extraCandies >= the maximum value in the 'candies' list, then add True to the boolean list; otherwise, add False to the boolean list.
3. Return the boolean list.
Time complexity of O(n)

"""