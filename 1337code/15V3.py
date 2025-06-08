class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                l = i + 1
                r = len(nums) - 1
                t = -nums[i]

                while l < r:
                    if l != i + 1 and nums[l - 1] == nums[l]:
                        l += 1
                        continue
                    if r != len(nums) - 1 and nums[r + 1] == nums[r]:
                        r -= 1
                        continue
                    
                    s = nums[l] + nums[r]

                    if s > t:
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        r -= 1
                        l += 1
        
        return res

s = Solution()

print(s.threeSum([-2, 1, 1, 1, 1]))