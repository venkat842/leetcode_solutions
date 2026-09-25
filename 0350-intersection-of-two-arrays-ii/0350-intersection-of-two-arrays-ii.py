class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        op = []
        if len(nums1) > len(nums2):
           for i in nums2:
               if i in nums1:
                  op.append(i)
                  nums1.remove(i)
        else:
            for i in nums1:
                if i in nums2:
                    op.append(i)
                    nums2.remove(i)
        return op
