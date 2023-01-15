class Solution:
    def twoSum(self, nums: List[int], target: int) :
        ans = []
        n = len(nums)
        if nums[n-1] + nums[n-2] == target :
            return [n-2,n-1]
        for i in range(len(nums)-1) :
            for j in range(i+1,len(nums)) :
                if nums[i]+nums[j] == target :
                    ans = ans+[i]+[j]
                    return ans