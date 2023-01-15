class Solution:
    def isIsomorphic(self, s: str, t: str) :
        if len(set(s)) == len(set(t)) == len(set(zip_longest(s,t))) :
            return True
        return False