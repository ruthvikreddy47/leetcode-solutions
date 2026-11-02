class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        
        return False
        