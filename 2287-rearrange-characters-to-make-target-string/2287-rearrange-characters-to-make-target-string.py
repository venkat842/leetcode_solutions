class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = list(s)
        valid = True
        word = ""
        count = 0
        while valid:
            for i in target:
                if i in s:
                    word += i
                    s.remove(i)
                    if len(word) == len(target):
                        count += 1 
                        word = ""
                else:
                    valid = False
                    break
        return count