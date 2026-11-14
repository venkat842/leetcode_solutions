class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        op = []
        for i in range(1,mn+1):
            if mn % i == 0 and mx % i == 0:
                op.append(i)
        return max(op)