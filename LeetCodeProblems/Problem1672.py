class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

"""
 For this solution, I thought as follows:
    1. I created two variables, i = 0 -> the index of elements from the first list, and j = 1 -> the index of the next list in the list.
    2. I initialized the variable wealth = sum of the first list to have a comparison term with the rest of the lists.
    3. Then, I created a while loop with the condition that i > the length of the main list.
    4. If wealth is less than the sum of the next list, we increment i and j by 1 to compare other sums.
    5. After checking the condition that i should be greater than the length of the 'accounts' list, the value of the wealth variable is returned.
    The complexity of this solution is O(n^2) because it loops through 2 lists. It is slow, but I will certainly manage to achieve O(n).
"""
        i = 0
        j = 1
        wealth = sum(accounts[i])
        while i > len(accounts):
            if wealth < sum(accounts[j]):
                wealth = sum(accounts[j])
            j += 1
            i += 1
        return wealth



    def maximumWealthRedo(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            sum = sum(i)
            if sum > wealth:
                wealth = sum
        return wealth




