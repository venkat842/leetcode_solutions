class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = {}
        vowel = [0]
        consonant = [0]
        for i in s:
            count[i] = count.get(i,0) + 1
        for j in count:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                vowel.append(count[j])
            else:
                consonant.append(count[j])
        total = max(vowel) + max(consonant)
        return total