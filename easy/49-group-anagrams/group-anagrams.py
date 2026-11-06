class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        dicts = []

        for s in strs:
            out = {}
            for char in s:
                out[char] = out.get(char, 0) + 1
            dicts.append(out)

        print(dicts)
        visited = set()

        for i in range(len(strs)):
            if i in visited:
                continue
            
            current_group = [strs[i]]
            visited.add(i)
            for j in range( i + 1, len(strs)):

                if j in visited:
                    continue

                if dicts[i] == dicts[j]:
                    current_group.append(strs[j])
                    visited.add(j)
            
            res.append(current_group)

        return res
                

        