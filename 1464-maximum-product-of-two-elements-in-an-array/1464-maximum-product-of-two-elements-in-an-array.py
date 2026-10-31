class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        op = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    op.append((nums[i]-1) * (nums[j]-1))
        return max(op)