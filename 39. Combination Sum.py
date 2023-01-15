class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cand,s,target,d) :
            if s == target :
                res.append(sorted(d.copy()))
            if s>target :
                return
            for x in range(len(cand)) :
                d.append(cand[x])
                dfs(cand,s+cand[x],target,d)
                d.pop()
        
        dfs(candidates,0,target,[])
        ans = []
        for x in res :
            if x in ans :
                continue
            ans.append(x)
        return ans