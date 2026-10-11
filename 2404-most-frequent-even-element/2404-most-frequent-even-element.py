class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            if nums.count(i) > count and i % 2 == 0:
                count = nums.count(i)
        element = []
        for i in nums:
            if i % 2 == 0:
                if nums.count(i) == count:
                    element.append(i)
        if not element:
            return -1
        else:
            return min(element)