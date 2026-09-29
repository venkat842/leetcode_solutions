class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        for i in nums.copy():
            i = int(str(i)[::-1])
            nums.append(i)
        return len(set(nums))
