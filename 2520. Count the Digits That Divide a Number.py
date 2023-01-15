class Solution:
    def countDigits(self, num: int) :
        n = num
        ans = 0
        lst = []
        while num>0:
            lst.append(num%10)
            num = (num-(num%10))/10
        for i in range(len(lst)) :
            if n%lst[i] == 0 :
                ans+=1
        return ans
        