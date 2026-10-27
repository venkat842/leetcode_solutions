class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if k == 1:
            return 0
        op = []
        nums.sort()
        for i in range(len(nums) - k + 1):
            a = abs(nums[i] - nums[i + k - 1])
            op.append(a)
        return min(op)
                