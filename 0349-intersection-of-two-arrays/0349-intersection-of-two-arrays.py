class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        op = []
        for i in nums1:
            if i in nums2:
                op.append(i)
        return op

