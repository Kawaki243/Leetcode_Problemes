class Solution:
    def bestClosingTime(self, customers: str) :
        s = 0
        y = 0
        ans = []
        c = collections.defaultdict(int)
        if customers == 'N'*len(customers) :
            return 0
        if customers == 'Y'*len(customers) :
            return len(customers)
        for j in range(len(customers)) :
            if customers[j] == 'Y' :
                s = s+1
            if customers[j] == 'N' :
                y = y+1
        lst = [0]*(len(customers)+1)
        lst[0] = s
        for i in range(1,len(customers)) :
            if i == 1 :
                if customers[i-1] == 'Y' :
                    lst[i] = s-1
                if customers[i-1] == 'N' :
                    lst[i] = s+1
            else :
                if customers[i-1] == 'Y' :
                    lst[i] = lst[i-1]-1
                elif customers[i-1] == 'N':
                    lst[i] = lst[i-1]+1
        lst[len(customers)] = y
        for j in range(len(lst)) :
            c[j] +=lst[j]
        sorted_sc = sorted(c.items(),key = lambda x : x[1])
        return sorted_sc[0][0]