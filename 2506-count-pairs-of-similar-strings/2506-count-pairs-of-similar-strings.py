class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0
        n = len(words)
        for i in range(n):
            set_a = set(words[i])
            for j in range(i+1,n):
                set_b = set(words[j])
                if set_a == set_b:
                  count += 1
        return count