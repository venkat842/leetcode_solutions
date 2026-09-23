class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        miss_list = []
        max_element = len(nums)
        for i in range(1,max_element+1):
            if i not in num_set:
                miss_list.append(i)
        return miss_list