class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        op = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                op.append(i)
        return op