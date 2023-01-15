class Solution:
    def strStr(self, haystack: str, needle: str) :
        n = len(needle)
        l = len(haystack)
        for i in range(l-n+1) :
            if haystack[i:i+n] == needle :
                return i
        return -1