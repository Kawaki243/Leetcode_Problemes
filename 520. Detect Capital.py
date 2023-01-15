class Solution:
    def detectCapitalUse(self, word: str) :
        st1 = 'abcdefghijklmnopqrstuvwxyz'
        st2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = 0
        if word[0] in st2 :
            for i in range(1,len(word)) :
                if word[i] in st2 :
                    n = n+1
            if n == len(word)-1 or n == 0:
                return True
            else :
                return False
        else :
            for i in range(1,len(word)) :
                if word[i] in st2 :
                    return False
            return True
             