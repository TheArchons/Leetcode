#code here
import math

class Solution:
    def binarySearchClosest(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return nums[mid]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left == right:
            left -= 1
        if abs(nums[left] - target) < abs(nums[right] - target):
            return nums[left]
        else:
            return nums[right]

    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        result = math.inf
        #iterate through all possible combinations of two numbers
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                find = target - nums[i] - nums[j]
                #find the closest number to the target
                temp = []
                for pos, k in enumerate(nums):

                    if pos != i and pos != j:
                        temp.append(k)
                closest = self.binarySearchClosest(self, temp, find)

                #if the closest number is the target, return the target
                if closest == find:
                    return target
                #compare if result or sum is closer to target
                sum = nums[i] + nums[j] + closest
                if abs(sum - target) < abs(result - target):
                    result = sum

        return result


nums = input().strip('[]').split(',')
nums = [int(x) for x in nums]
target = int(input())
print(Solution.threeSumClosest(Solution, nums, target))