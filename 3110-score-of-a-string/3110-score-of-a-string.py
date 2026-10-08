class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            a = ord(s[i])
            b = ord(s[i+1])
            c = abs(a - b)
            total += c
        return total
