class Solution:
    def frequencySort(self, s: str) :
        sc = defaultdict(int)
        ans = ''
        for i in range(len(s)) :
            sc[s[i]] +=1
        sorted_sc = sorted(sc.items(),key = lambda x : x[1],reverse = True)
        for j in range(len(sorted_sc)) :
            ans = ans+(sorted_sc[j][0]*sorted_sc[j][1])
        return ans