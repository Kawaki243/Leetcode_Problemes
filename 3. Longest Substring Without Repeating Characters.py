class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int abcabcbb
        """
        freq = set()
        l = 0
        res = 0
        for r in range(len(s)) :
            while s[r] in freq :
                freq.remove(s[l])
                l = l+1
            freq.add(s[r])
            res = max(res,r-l+1)
        return res