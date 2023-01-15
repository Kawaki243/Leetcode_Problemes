class Solution:
    def reverse(self, x: int) :
        n = 0
        m = abs(x)
        ans = 0
        lst = []
        while m>0 :
            n = n+1
            lst.append(m%10)
            m = (m-(m%10))/10
        if x > 0 :
            for i in range(len(lst)) :
                ans = ans+lst[i]*(10**(len(lst)-1-i))
            if 2**31-1<int(ans) :
                return 0
            else :
                return int(ans)
        else :
            for i in range(len(lst)) :
                ans = ans+lst[i]*(10**(len(lst)-1-i))
            if -int(ans)<-2**31 :
                return 0
            else :
                return -int(ans)