class Solution:
    def romanToInt(self, s: str) :
        t = 0
        n = len(s)
        if 'IV' in s :
            t = t+4
            s = s.replace('IV','')
        if 'IX' in s :
            t = t+9
            s = s.replace('IX','')
        if 'XL' in s :
            t = t+40
            s = s.replace('XL','')
        if 'XC' in s :
            t = t+90
            s = s.replace('XC','')
        if 'CD' in s :
            t = t+400
            s = s.replace('CD','')
        if 'CM' in s :
            t = t+900
            s = s.replace('CM','')
        for i in range(len(s)) :
            if s[i] == 'I' :
                t = t+1
            if s[i] == 'V' :
                t = t+5
            if s[i] == 'X' :
                t = t+10
            if s[i] == 'L' :
                t = t+50
            if s[i] == 'C' :
                t = t+100
            if s[i] == 'D' :
                t = t+500
            if s[i] == 'M' :
                t = t+1000
        return t
