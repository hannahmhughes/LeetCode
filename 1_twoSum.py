class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}

        for i in range(len(nums)): 

            value = nums[i]
            complement = target - value

            if complement in pairs: 
                return [pairs[complement], i]
            else: 
                pairs[value] = i