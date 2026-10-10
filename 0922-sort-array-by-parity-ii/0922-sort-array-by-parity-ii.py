class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        op = []
        for i in nums:
            if i % 2 != 0:
                odd.append(i)
            else:
                even.append(i)
        for j in range(len(odd)):
            op.append(even[j])
            op.append(odd[j])
        return op