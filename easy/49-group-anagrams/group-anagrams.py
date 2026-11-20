class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        frequency = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            frequency[tuple(counts)].append(word)
        
        result = []
        for value in frequency.values():
            result.append(value)
        
        return result


        