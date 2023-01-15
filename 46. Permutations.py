class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(d,visited,ans,nums) :
            if len(d) == len(nums) :
                ans.append(d.copy())
                return
            for i in range(len(nums)) :
                if not visited[i] :
                    d.append(nums[i])
                    visited[i] = True
                    dfs(d,visited,ans,nums)
                    d.pop()
                    visited[i] = False
            
        d = []
        ans = []
        visited = [0]*len(nums)
        dfs([],visited,ans,nums)
        return ans