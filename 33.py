from re import L


def search(nums, target):
    first = nums[0]
    left, right = 0, len(nums)-1
    curr = int(len(nums)/2)
    if first == target:
        return 0
    while nums[curr] != target:
        if target < first:
            if nums[curr] > first:
                curr += int((right-curr)/2)
            elif nums[curr] < target:
                curr += int((right-curr)/2)
            else:
                curr -= int((curr-left)/2)
        elif nums[curr] > target:
            curr -= int((curr-left)/2)
        else:
            curr += int((right-curr)/2)
    return curr

ins = input().strip('[]').split(',')
target = int(input())
inArr = [int(i) for i in ins]
print(search(inArr, target))

"""
curr += int((right-curr)/2) #increase
curr -= int((curr-left)/2) #decrease


"""