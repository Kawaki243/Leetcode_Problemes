import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) :
        m = len(matrix[0])
        n = len(matrix)
        ans = copy.deepcopy(matrix)
        j = 0
        while j < m:
            for i in range(n) :
                matrix[j][i] = ans[n-1-i][j]
            j = j+1
        