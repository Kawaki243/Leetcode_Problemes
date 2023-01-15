import copy
class Solution:
    def minDeletionSize(self, strs: List[str]) :
        n = len(strs[0])
        lst = []
        m = 0
        j = 0
        while j<n :
            ans = []
            for i in strs :
                ans.append(i[j])
            lst.append(ans)
            j = j+1
        lst1 = copy.deepcopy(lst)
        for c in lst :
            c.sort()
        for d in range(len(lst)) :
            if lst1[d] != lst[d] :
                m = m+1
        return m