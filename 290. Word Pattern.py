class Solution:
    def wordPattern(self, pattern: str, s: str) :
        s = s.split()
        if len(set(s)) == len(set(pattern)) == len(set(zip_longest(pattern,s))) :
            return True
        return False