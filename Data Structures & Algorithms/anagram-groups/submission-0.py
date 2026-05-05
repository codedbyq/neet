class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # key is sorted chars, value is list of matches
        for string in strs:
            key = "".join(sorted(string))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [ string ]
        return list(anagrams.values())