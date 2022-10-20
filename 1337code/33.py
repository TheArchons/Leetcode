def search(nums, target):
    first = nums[0]
    left, right = 0, len(nums)-1
    curr = int(len(nums)/2)
    if first == target:
        return 0
    if nums[-1] == target:
        return len(nums)-1
    while nums[curr] != target and left < right-1:
        if target < first:
            if nums[curr] > first:
                left = curr
                curr += int((right-curr)/2)
            elif nums[curr] < target:
                left = curr
                curr += int((right-curr)/2)
            else:
                right = curr
                curr -= int((curr-left)/2)
        elif nums[curr] > target or nums[curr] < first:
            right = curr
            curr -= int((curr-left)/2)
        else:
            left = curr
            curr += int((right-curr)/2)
    if nums[curr] == target:
        return curr
    return -1

ins = input().strip('[]').split(',')
target = int(input())
inArr = [int(i) for i in ins]
print(search(inArr, target))

"""
curr += int((right-curr)/2) #increase
curr -= int((curr-left)/2) #decrease
"""