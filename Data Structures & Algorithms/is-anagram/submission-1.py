class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        for char in s:
            dictS[char] = dictS.get(char, 0) + 1

        dictT = {}
        for char in t:
            dictT[char] = dictT.get(char, 0) + 1

        return dictS == dictT
