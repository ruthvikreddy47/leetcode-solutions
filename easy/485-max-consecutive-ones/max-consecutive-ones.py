class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for val in nums:
            if val == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0

        return result
        