def search(nums, target):
    numLen = len(nums)
    if nums[0] == target:
        return 0
    min = 0
    max = numLen
    while max-min != 1:
        check = int((numLen - min - (numLen - max))/2)+min
        if nums[check] == target:
            return check
        elif nums[check] < target:
            min = check
        else:
            max = check 
    return -1
        
ins = input()
nums = [int(i) for i in ins.split(',')]
target = int(input())
print(search(nums, target))