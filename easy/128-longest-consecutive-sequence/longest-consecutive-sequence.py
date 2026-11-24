class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums_set = set(nums)
        count = 0
        longest_seq = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            while num in nums_set:
                num += 1
                count += 1
            longest_seq = max(count, longest_seq)
            count = 0
        
        return longest_seq
        