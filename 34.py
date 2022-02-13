def searchRange(nums, target):
    #find the first index of the target
    try:
        pos = nums.index(target)
    except ValueError:
        return [-1,-1]
    #find the last index of the target
    iPos = 0
    for i in nums[pos+1:]:
        if i != target:
            return [pos, pos + iPos]
        iPos += 1
    return [pos, pos+iPos]
    
nums = input().strip('[]').split(',')
nums = [int(i) for i in nums]
target = int(input())
print(searchRange(nums, target))