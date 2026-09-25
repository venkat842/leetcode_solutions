class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        op1 = list(set(nums1) - set(nums2))
        op2 = list(set(nums2) - set(nums1))
        return [op1,op2]