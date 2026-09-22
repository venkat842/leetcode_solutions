class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        list_nums = list(map(int,num))

        while len(list_nums) > 1:
           list_nums = sum(list_nums)
           list_nums = str(list_nums)
           list_nums = list(map(int,list_nums))
        return list_nums[0]
