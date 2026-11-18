class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        if coordinate1[0] == 'a' or coordinate1[0] == 'c' or coordinate1[0] == 'e' or coordinate1[0] == 'g':
            if int(coordinate1[1]) % 2 == 0:
                color1 = 'White'
            else:
                color1 = 'Black'
        else:
            if int(coordinate1[1]) % 2 == 0:
                color1 = 'Black'
            else:
                color1 = 'White'
        if coordinate2[0] == 'a' or coordinate2[0] == 'c' or coordinate2[0] == 'e' or coordinate2[0] == 'g':
            if int(coordinate2[1]) % 2 == 0:
                color2 = 'White'
            else:
                color2 = 'Black'
        else:
            if int(coordinate2[1]) % 2 == 0:
                color2 = 'Black'
            else:
                color2 = 'White'
        return color1 == color2
        
