class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        op = []
        for i in nums:
            if i % 2 == 0:
                op.append(i)
        for i in nums:
            if i % 2 != 0:
                op.append(i)
        return op