class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = str(num1).zfill(4)
        num2 = str(num2).zfill(4)
        num3 = str(num3).zfill(4)
        a = min(int(str(num1)[0]), int(str(num2)[0]), int(str(num3)[0]))
        b = min(int(str(num1)[1]), int(str(num2)[1]), int(str(num3)[1]))
        c = min(int(str(num1)[2]), int(str(num2)[2]), int(str(num3)[2]))
        d = min(int(str(num1)[3]), int(str(num2)[3]), int(str(num3)[3]))
        result = str(a) + str(b) + str(c) + str(d)
        return int(result)