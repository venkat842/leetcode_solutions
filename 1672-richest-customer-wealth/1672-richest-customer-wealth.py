class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        op = []
        for i in accounts:
            op.append(sum(i))
        return max(op)
