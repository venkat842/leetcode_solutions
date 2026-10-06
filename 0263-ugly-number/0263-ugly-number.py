class Solution:
    def isUgly(self, n: int) -> bool:
        f = [2,3,5]
        if n<=0:
            return False
        for i in f:
            while n % i == 0:
                n //= i
        return n == 1