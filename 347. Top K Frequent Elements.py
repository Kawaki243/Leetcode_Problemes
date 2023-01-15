class Solution:
    def topKFrequent(self, nums: List[int], k: int) :
        ans = []
        c = defaultdict(int)
        for i in nums :
            c[i] +=1
        sorted_c = sorted(c.items(),key = lambda x : x[1], reverse = True)
        for j in range(k) :
            ans.append(sorted_c[j][0])
        return ans