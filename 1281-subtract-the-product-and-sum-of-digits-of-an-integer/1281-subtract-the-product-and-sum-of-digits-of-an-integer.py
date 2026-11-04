class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for i in str(n):
            digit = int(i)
            product *= digit
            total += digit
        return product - total