class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}
        # iterate through strings
        for string in strs:
            # create a lookup key based on the characters in each string 
            key = "".join(sorted(string)) # sorted returns a list so we need to join back to a string for key to work in dict
            # check if key exists 
            if key in sublists:
                # if so, append current string
                sublists[key].append(string)
            else:
                # else create the group
                sublists[key] = [ string ]
        # after loop return values of the dict
        return list(sublists.values())
