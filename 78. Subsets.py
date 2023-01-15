class Solution:
    def subsets(self, nums: List[int]) :
        n = len(nums)
        ans = []
        def dfs(i,subset) :
            if i>= n:
                ans.append(subset)
                return 
            dfs(i+1,subset+[nums[i]])
            dfs(i+1,subset)
        dfs(0,[])
        return ans