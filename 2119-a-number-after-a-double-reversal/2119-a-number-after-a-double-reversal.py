class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num_str = str(num)
        reversed1 = str(int(num_str[::-1]))
        reversed2 = reversed1[::-1]
        return int(reversed2) == num