class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)
        result = []

        for s in strs:
            key = tuple(self.countLettersArray(s))
            group[key].append(s)
        
        for val in group.values():
            result.append(val)
        
        return result

    
    def countLettersArray(self, s: str)-> list[int]:
        count = [0] * 26

        for letter in s:
            count[ord(letter) - ord('a')] += 1
        
        return count

        