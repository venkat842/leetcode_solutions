class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = list(magazine)
        valid = True
        for i in ransomNote:
            if i in chars:
                chars.remove(i)
            else:
                valid = False
                break
        return valid
