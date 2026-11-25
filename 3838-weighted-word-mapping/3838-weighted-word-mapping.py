class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        op = ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        rev = "zyxwvutsrqponmlkjihgfedcba"
        for i in words:
            total = 0
            for j in i:
                total += weights[alpha.index(j)]
            result = total % 26
            op += rev[result]
        return op