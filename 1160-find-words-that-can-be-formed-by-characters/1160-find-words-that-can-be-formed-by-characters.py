class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        total = 0
        chars = list(chars)
        for i in words:
            temp_chars = chars.copy()
            valid = True
            for j in i:
                if j in temp_chars:
                    temp_chars.remove(j)
                else:
                    valid = False
                    break
            if valid:
                total += len(i)
        return total
