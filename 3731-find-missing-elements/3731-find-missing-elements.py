class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        op = []
        for i in range(min(nums),max(nums)):
            if i not in nums:
                op.append(i)
        return op