class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = []
        double = []
        for i in nums:
            length = len(str(i))
            if length == 1:
                single.append(i)
            else:
                double.append(i)
        return (sum(single) > sum(double)) or (sum(double) > sum(single))

