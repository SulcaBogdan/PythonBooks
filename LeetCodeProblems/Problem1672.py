class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        i = 0
        j = 1
        wealth = sum(accounts[i])
        while i > len(accounts):
            if wealth < sum(accounts[j]):
                wealth = sum(accounts[j])
            j += 1
            i += 1
        return wealth







