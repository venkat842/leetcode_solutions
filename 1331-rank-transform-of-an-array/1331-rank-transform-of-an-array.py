class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        b = sorted(list(set(arr)))
        rank = {}
        for i in range(len(b)):
            rank[b[i]] = i + 1 
        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        return arr
