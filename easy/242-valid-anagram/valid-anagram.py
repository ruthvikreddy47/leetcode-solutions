class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
             return False

        return self.toDict(s) == self.toDict(t)

    def toDict(self, s: str):
        res = {}

        for char in s:
            if char in res:
                val = res.get(char)
                val = val + 1
                res[char] = val
            else:
                res[char] = 1
        
        return res
        