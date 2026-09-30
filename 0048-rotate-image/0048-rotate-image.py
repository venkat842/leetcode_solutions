class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        op = []
        
        for i in range(n):
            new = []
            for j in range(n - 1, -1, -1):
                new.append(matrix[j][i])
            
            op.append(new)
    
        matrix[:] = op