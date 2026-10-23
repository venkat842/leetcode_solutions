class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i,0) + 1 
        op = []
        for i in counts:
            if counts[i] == 1:
                op.append(i)
        return op