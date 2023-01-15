class Solution:
    def searchRange(self, nums: List[int], target: int) :
        ans = []
        lst = []
        for i in range(len(nums)) :
            if nums[i] == target :
                ans.append(i)
        if len(ans) == 0 :
            lst = [-1,-1]
        elif len(ans) == 1 :
            lst = [ans[0],ans[0]]
        else :
            lst= lst+[ans[0]]+[ans[len(ans)-1]]
        return lst