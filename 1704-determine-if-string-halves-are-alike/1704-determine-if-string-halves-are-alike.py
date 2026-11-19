class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        lenght = len(s)
        a = s[:int(lenght/2)]
        count_1 = 0
        b = s[int(lenght/2):]
        count_2 = 0
        for i in a:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                count_1 += 1 
        for i in b:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                count_2 += 1 
        return count_1 == count_2
        


