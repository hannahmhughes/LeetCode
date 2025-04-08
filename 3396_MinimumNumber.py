class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numSet = set() 
        latestRepeat = -1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in numSet:
                return math.ceil((i + 1)/3)
            
            numSet.add(nums[i])
        
        return 0