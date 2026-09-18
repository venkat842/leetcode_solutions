class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list_ = s.split()
        result = len(list_[-1])
        return result