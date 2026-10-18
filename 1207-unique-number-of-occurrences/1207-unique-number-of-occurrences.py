class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        for i in arr:
            count[i] = count.get(i,0) + 1 
        unique = set()
        for i in arr:
            unique.add(count[i])
        return len(unique) == len(count)