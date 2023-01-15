class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        curr_num = nums[0]
        for i in range(n-1) :
            if nums[i]>curr_num :
                curr_num = nums[i]
            if curr_num == 0 :
                return False
            curr_num -=1
        return True
            
