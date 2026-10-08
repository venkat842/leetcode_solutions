class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        total = 0
        for i in nums:
            count = nums.count(i)
            if count == 1:
                total += i
        return total