class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        list_p = []
        list_n = []
        op = []
        for i in nums:
            if i < 0:
                list_n.append(i)
            else:
                list_p.append(i)
        for i in range(len(list_p)):
            op.append(list_p[i])
            op.append(list_n[i])
        return op