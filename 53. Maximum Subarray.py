class Solution:
    def maxSubArray(self, nums: List[int]) :
        arr = []
        arr.append(nums[0])
        mx = nums[0]
        for i in range(1,len(nums)) :
            arr.append(max(arr[i-1]+nums[i],nums[i]))
            if arr[i]>mx :
                mx = arr[i]
        return mx