class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    ans.append((i,j))
        
        for x in range(len(ans)) :
            for m in range(len(matrix[0])) :
                matrix[ans[x][0]][m] = 0
            for n in range(len(matrix)) :
                matrix[n][ans[x][1]] = 0
