class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_alpha = "zyxwvutsrqponmlkjihgfedcba"
        total = 0
        num1 = 1
        for i in s:
           num2 = rev_alpha.index(i) + 1 
           product = num1 * num2
           total += product
           num1 += 1
        return total