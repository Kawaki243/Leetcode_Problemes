class Solution:
    def subsetsWithDup(self, nums: List[int]) :
        ans = []
        nums.sort()
        i = 0
        def dfs(index,path) :
            ans.append(path)
            for i in range(index,len(nums)) :
                if i>index and nums[i] == nums[i-1] :
                    continue
                dfs(i+1,path+[nums[i]])
        dfs(0,[])
        return ans