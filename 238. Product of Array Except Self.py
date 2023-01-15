class Solution:
    def productExceptSelf(self, nums: List[int]) :
        res = []
        d = 1
        m = -1
        if len(nums) == 1 or len(nums) == 0 :
            return nums
        if nums.count(0)>1 :
            res = [0]*len(nums)
        if nums.count(0) == 1 :
            for j in range(len(nums)) :
                if nums[j] == 0 :
                    m = j
                    d = d*1
                else :
                    d = d*nums[j]
            for i in range(len(nums)) :
                if i!= m :
                    res.append(0)
                if i == m :
                    res.append(d)
        if nums.count(0) == 0 :
            for i in range(len(nums)) :
                d = d*nums[i]
            for j in range(len(nums)) :
                s = int(d//nums[j])
                res.append(s)
        return res