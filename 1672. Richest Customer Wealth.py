class Solution:
    def maximumWealth(self, accounts: List[List[int]]) :
        mx = -1
        s = 0
        ans = []
        for i in range(len(accounts)) :
            s = 0
            for j in range(len(accounts[i])) :
                s = s + accounts[i][j]
            mx = max(mx,s)
        return mx