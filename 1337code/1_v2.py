class Solution:
    def twoSum(nums, target: int):
        numDict = {}

        for i in range(len(nums)):
            numDict[nums[i]] = i
        
        for i in range(len(nums)):
            invNum = target - nums[i]

            if (numDict.get(invNum)):
                if (i == numDict[invNum]):
                    continue
                return [i, numDict[invNum]]
