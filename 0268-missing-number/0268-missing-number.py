class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)
        i = 0 
        while i in num_set:
            i += 1 
        return i 
        