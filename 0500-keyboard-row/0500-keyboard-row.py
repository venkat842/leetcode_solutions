class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        op = []
        for i in words:
            a = ""
            for j in i.lower():
                if j in first:
                    a += "1"
                elif j in second:
                    a += "2"
                elif j in third:
                    a += "3"
            if len(set(a)) == 1:
                op.append(i)
        return op