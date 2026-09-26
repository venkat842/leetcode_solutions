class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1 = s1.split()
        s2 = s2.split()
        s1.extend(s2)
        s3 = []
        for i in s1:
            if s1.count(i) == 1:
                s3.append(i)
        return s3
            