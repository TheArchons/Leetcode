class Solution:
    def searchInsert(self, nums, target):
        #binary search for the target
        start, end = 0, len(nums)-1
        pos = end//2

        while start <= end:
            if nums[pos] == target:
                return pos
            elif nums[pos] > target:
                end = pos - 1
            else:
                start = pos + 1
            pos = (start + end)//2
        return start

list = [int(i) for i in input().strip('[]').split(',')]
target = int(input())

print(Solution.searchInsert(Solution, list, target))
