class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        ans = 0
        for word in set(words2):
            if words1.count(word) == 1 and words2.count(word) == 1:
                ans += 1
        return ans