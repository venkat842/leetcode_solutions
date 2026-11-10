class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [''] * len(s)

        for i in range(len(s)):
            result[indices[i]] = s[i]

        shuffled_string = ''.join(result)
        return shuffled_string