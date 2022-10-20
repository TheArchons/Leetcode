class Solution:
    def removeDuplicates(self, nums):
        toPop = []
        for pos, i in enumerate(nums):
            if i == nums[pos - 1] and pos > 0:
                toPop.append(pos)
        for i in toPop[::-1]:
            nums.pop(i)
        return len(nums)

ins = input().strip('[]').split(',')
nums = [int(i) for i in ins]
s = Solution()
print(s.removeDuplicates(nums))