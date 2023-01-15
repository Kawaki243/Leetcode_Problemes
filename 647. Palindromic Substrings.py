class Solution:     
    def countSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)
        for i in range(n) :
            for j in range(i+1,n+1) :
                if s[i:j] == s[i:j][::-1] :
                    c = c+1
        return c

        