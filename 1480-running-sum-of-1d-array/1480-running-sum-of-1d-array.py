class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        op = []
        for i in nums:
            sum += i 
            op.append(sum)
        return op
