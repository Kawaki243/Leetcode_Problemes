class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums.copy()
        tmp.sort()        
        n = len(nums)
        i, j = 1, n - 1
        for _ in range(2): 
            for k in range(i, n, 2): # when i == 1 then gt elements and when i == 0 then sm elements with jump of 2
                nums[k] = tmp[j] # sorted array tmp reverse order values assignment
                j -= 1
            i -= 1