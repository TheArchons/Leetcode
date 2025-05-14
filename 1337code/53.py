class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = nums[0]

        for num in range(1, len(nums)):
            currSub = max(currSub, 0)
            currSub += nums[num]
            maxSub = max(currSub, maxSub)
        
        return maxSub