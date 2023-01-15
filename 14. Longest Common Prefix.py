class Solution:
    def longestCommonPrefix(self, strs: List[str]) :
        size = len(strs[0])
        res = ''
        for i in range(size) :
            for s in strs :
                if i == len(s) or s[i] != strs[0][i] :
                    return res
            res = res+strs[0][i]
        return res