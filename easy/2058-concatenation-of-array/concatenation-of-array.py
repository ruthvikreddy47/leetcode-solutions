class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = list(nums);

        for val in nums:
           result.append(val);
        
        return result;
        