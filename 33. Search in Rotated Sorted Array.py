class Solution:
    def search(self, nums: List[int], target: int) :
        x = -1
        for i in range(len(nums)) :
            if nums[i] == target :
                x = i
        return x