class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sum_ = []
        for i in range(len(accounts)):
            sum_.append(sum(accounts[i]))
        return max(sum_)