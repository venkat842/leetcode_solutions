class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        a = heights.copy()
        a.sort()
        count = 0
        for i in range(len(a)):
            if a[i] != heights[i]:
                count += 1 
        return count