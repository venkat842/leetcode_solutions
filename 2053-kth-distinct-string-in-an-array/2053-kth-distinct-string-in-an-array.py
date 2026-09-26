class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        op = []
        for i in arr:
            if arr.count(i) == 1:
                op.append(i)
        if len(op) >= k:
            return op[k - 1]
        else:
            return ""