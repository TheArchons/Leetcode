def threeSum(nums):
    numberCounts = {}
    uniqueNumsArr = []
    temp = []
    for pos, i in enumerate(nums): #count the number of times each number appears, removing anything that appears more than 3 times
        if i in numberCounts:
            if numberCounts[i] >= 3:
                continue
            else:
                numberCounts[i] += 1
                temp.append(i)
        else:
            numberCounts[i] = 1
            temp.append(i)
    nums = temp
    
                    
 
    #check each combo of 2 numbers
    results = []
    for iPos, i in enumerate(nums):
        for jPos, j in enumerate(nums):
            if iPos >= jPos:
                continue
            numberCounts[i] -= 1
            numberCounts[j] -= 1
            searchNum = -(i + j)
            if searchNum in numberCounts and numberCounts[searchNum] > 0:
                results.append(sorted([i, j, searchNum]))
            numberCounts[i] += 1
            numberCounts[j] += 1

    #remove duplicates
    results = sorted(results)
    output = []
    prev = [-1, -1, -1]
    for pos, result in enumerate(results):
        if result == prev:
            continue
        else:
            output.append(result)
            prev = result
    return output

nums = input().strip('[]').split(',')
if (nums[0] == ''):
    print(threeSum(nums))
else:
    nums = [int(i) for i in nums]
    print(threeSum(nums))