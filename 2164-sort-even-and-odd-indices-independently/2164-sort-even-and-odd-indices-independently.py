class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        op = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd = sorted(odd,reverse = True)
        even = sorted(even)
        i = 0
        while i < len(odd):
            op.append(even[i])
            op.append(odd[i])
            i += 1 
        if len(even) > i:
            op.append(even[i])
        return op