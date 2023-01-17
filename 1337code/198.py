class Solution:
    def rob(self, nums) -> int:
        # base cases for 0, 1, 2, 3
        if len(nums) == 0:
            return 0

        first = nums[0]
        
        if len(nums) == 1:
            return first
        
        second = max(nums[0], nums[1])
        
        if len(nums) == 2:
            return second
        
        maxProfit = 0
        
        for i in range(2, len(nums)):
            curr = max(nums[i] + first, second)
            first = second
            second = curr
            maxProfit = max(maxProfit, curr)
        
        return maxProfit
        