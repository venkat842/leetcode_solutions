class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        arr1 = []
        arr2 = []
        for i in nums:
            arr1.append(left)
            left += i
        for j in reversed(nums):
            arr2.append(right)
            right += j
        arr2.reverse()
        ans = []
        for k in range(len(nums)):
            n = abs(arr1[k] - arr2[k])
            ans.append(n)
        return ans
        