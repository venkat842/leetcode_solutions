class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        unique_set = set()
        for i in nums:
            if i not in unique_set:
                unique_set.add(i)
            else:
                return i