class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) :
        lst = []
        ans = []
        s = 0
        n = len(mat)
        for i in range(n) :
            s = 0
            for j in range(len(mat[i])) :
                if mat[i][j] == 1 :
                    s = s+1
            lst.append((s,i))
        lst.sort()
        for j in range(k):
            ans.append(lst[j][1])
        return ans
    