class Solution:
    def findDuplicate(self, nums: List[int]) :
        c = defaultdict(int)
        for i in range(len(nums)) :
            c[nums[i]] +=1
        for y in c :
            if c[y]>1 :
                return y