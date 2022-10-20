def twoSum(nums, target):
    numDict = {}
    for i in range(len(nums)):
        if nums[i] in numDict:
            numDict[nums[i]] += 1
        else:
            numDict[nums[i]] = 1
    for i in range(len(nums)):
        numDict[i] -= 1
        if numDict[target-i] > 0:
            return [i, target-i]
        numDict[i] += 1
y = input().split()
#convert to int
y = [int(x) for x in y]
print(twoSum(y, int(input())))