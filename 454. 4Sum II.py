class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) :
        nums12= []
        t = 0
        for x in range(len(nums1)) :
            for y in range(len(nums2)) :
                for z in range(len(nums3)) :
                    for m in range(len(nums4)) :
                        nums12.append(nums1[x]+nums2[y]+nums3[z]+nums4[m])
        for i in range(len(nums12)) :
            if nums12[i] == 0:
                t = t+1              
        return t
              
