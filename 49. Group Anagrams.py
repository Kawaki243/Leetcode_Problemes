class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            HashofStrings = {}
            for string in strs :
                sortedString= ''.join(sorted(string))
                if sortedString in HashofStrings:
                    HashofStrings[sortedString].append(string)
                else:
                    HashofStrings[sortedString]=[string]
            return list(HashofStrings.values())
