class Solution:
    def permuteUnique(self, nums: List[int]) :
        path = []
        def dfs(d,visted,ans,nums) :
            if len(d) == len(nums) and d.copy() not in path :
                ans.append(d.copy())
                path.append(d.copy())
                return
            for i in range(len(nums)) :
                if not visited[i] :
                    d.append(nums[i])
                    visited[i] = True
                    dfs(d,visited,ans,nums)
                    d.pop()
                    visited[i] = False
        
        d = []
        visited = [0]*len(nums)
        ans = []
        dfs(d,visited,ans,nums)
        return ans