class Solution:
    def maxArea(self, height: List[int]) :
        mx = 0
        i = 0
        j = len(height)-1
        while j-i>=1 :
            if height[i]<height[j] :
                mx = max(mx,height[i]*(j-i))
                i = i +1
            elif height[i]>height[j] :
                mx = max(mx,height[j]*(j-i))
                j = j- 1
            else : 
                mx = max(mx,height[j]*(j-i))
                j = j-1
                i = i+1
        return mx