from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt=Counter(tasks)
        sm=0
        for i in cnt:
            if cnt[i]==1:
                return -1
            x=cnt[i]//3
            y=cnt[i]%3
            if y==0:
                sm+=x
            else:
                sm+=(x+1)
        return sm
                
            
        