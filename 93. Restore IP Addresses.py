class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        ans = []
        if size > 12 : 
            return []
        def dfs(i,d,c) :
            if i == size and d == 4 :
                ans.append(c[:-1])
                return
            if d>4 :
                return
            end_dots = min(i+3,size)

            for j in range(i,end_dots) :
                part = s[i:j+1]

                if int(part)<=255 and (i==j or s[i] != '0') :
                    dfs(j+1,d+1,c+part+'.')
        dfs(0, 0, '')
        return ans
