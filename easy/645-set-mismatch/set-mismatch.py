class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # n is the length of the input array
        n = len(nums)
        counts = {}
        
        # Count the frequency of each number
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        duplicate = -1
        missing = -1
        
        # Iterate through the expected range [1, n]
        for i in range(1, n + 1):
            if i in counts:
                if counts[i] == 2:
                    duplicate = i
            else:
                missing = i
        
        # Return result in specific order: [duplicate, missing]
        return [duplicate, missing]