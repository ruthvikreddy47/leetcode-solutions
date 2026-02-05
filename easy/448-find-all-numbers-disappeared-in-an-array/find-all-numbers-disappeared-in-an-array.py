class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_num = set(nums)
        result = []
        
        for i in range(1, len(nums) + 1):
            if i not in max_num:
                result.append(i)
        
        return result
        