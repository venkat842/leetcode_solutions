class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        op = []
        for i in range(left,right+1):
            valid = True
            if '0' not in str(i):
                for j in range(len(str(i))):
                      num = str(i)
                      if i % int(num[j]) != 0:
                           valid = False
                if valid:
                    op.append(i)
        return op
