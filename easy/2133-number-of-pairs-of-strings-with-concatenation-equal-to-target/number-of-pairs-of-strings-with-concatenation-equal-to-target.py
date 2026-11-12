class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:

        pairs = 0

        for i in range(len(nums)):
            for j in range( len(nums)):
                if i == j:
                    continue
                    
                con = f"{nums[i]}{nums[j]}"
                print(con,f"{i} {j}")
                if con == target:
                    pairs += 1
        
        return pairs
        