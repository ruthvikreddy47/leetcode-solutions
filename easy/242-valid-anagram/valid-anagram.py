class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
             return False

        return self.toDict(s) == self.toDict(t)

    def toDict(self, s: str):
        res = {}

        for char in s:
            res[char] = res.get(char, 0) + 1
        
        return res
        