class Solution:
    def combinationSum3(self, k: int, n: int) :
        ans = []
        path = []
        if 9*k<n or k>n:
            return []
        def dfs(i,d,s,visited) :
            if s == n and len(d.copy()) == k and sorted(d.copy()) not in path:
                ans.append(d.copy())
                path.append(sorted(d.copy()))
                return
            if s>n or len(d.copy())>k or i>9:
                return
            for j in range(i,10) :
                if not visited[j] :
                    visited[j] = True
                    dfs(j+1,d+[j],s+j,visited)
                    visited[j] = False
        visited = [0]*10            
        dfs(1,[],0,visited)
        return ans