class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i,0) + 1 
        result = 0
        for i in counts:
            if counts[i] == 2:
                result ^= i 
        return result