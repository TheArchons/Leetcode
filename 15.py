def threeSum(nums):
    results = []
    #loop through nums
    for iPos, i in enumerate(nums):
        for jPos, j in enumerate(nums):
            for zPos, z in enumerate(nums):
                if iPos != jPos and iPos != zPos and jPos != zPos:
                    if i + j + z == 0:
                        finalNums = [i, j, z]
                        finalNums.sort()
                        if finalNums not in results:
                            results.append(finalNums)
    return results

ins = input().split(',')
#convert to ints
ins = [int(i) for i in ins]
print(threeSum(ins))