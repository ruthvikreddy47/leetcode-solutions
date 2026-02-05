class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_count = 0
        num_count_map = {}

        idx = 0
        for i in range(len(nums)):
            if nums[i] in num_count_map and num_count_map.get(nums[i]) >= 2:
                duplicate_count = duplicate_count + 1
            else:
                num_count_map[nums[i]] = num_count_map.get(nums[i], 0) + 1
                nums[idx] = nums[i]
                idx = idx + 1
        
        return len(nums) - duplicate_count
                
