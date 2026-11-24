class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        left_arr = [1] * (len(nums))
        right_arr = [1] * (len(nums))
        result = []

        left_prod = 1
        right_prod = 1
        i = 0
        j = len(nums) - 1

        while i < len(nums):
            left_arr[i] = left_prod
            right_arr[j] = right_prod

            left_prod *= nums[i]
            right_prod *= nums[j]

            i += 1
            j -= 1
        
        i = 0
        while i < len(left_arr):
            result.append(left_arr[i] * right_arr[i])
            i += 1
        
        return result


            
        