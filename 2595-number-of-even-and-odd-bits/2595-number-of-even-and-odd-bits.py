class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        odd = 0
        even = 0
        bit_num = format(n,"b")
        bit_num = bit_num[::-1]
        for i in range(len(bit_num)):
            if i % 2 == 0 and bit_num[i] == '1':
                even += 1 
            elif i % 2 != 0 and bit_num[i] == '1':
                odd += 1 
        return [even,odd]
        