class Solution:
    longestSubsequence = 0
    

    def isIncreasing(self, nums):
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True

    def recurseRemove(self, nums):
        if (len(nums) == 0):
            return
        
        if self.isIncreasing(nums):
            self.longestSubsequence = max(self.longestSubsequence, len(nums))
            return
        
        for i in range(len(nums)):
            self.recurseRemove(nums[:i] + nums[i+1:])

    def lengthOfLIS(self, nums) -> int:
        if self.isIncreasing(nums):
            return len(nums)

        self.recurseRemove(nums)
        return self.longestSubsequence
