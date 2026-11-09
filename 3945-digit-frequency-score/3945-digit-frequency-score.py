class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        count = {}
        for i in n:
            digit = int(i)
            count[digit] = count.get(digit,0) + 1   
        score = 0
        for digit,occur in count.items():
            a = digit * occur
            score += a 
        return score