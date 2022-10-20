import math

def median(nums):
    if len(nums) % 2 == 0:
        return (nums[len(nums)//2] + nums[len(nums)//2-1])/2
    else:
        return nums[len(nums)//2]

def findMedianSortedArrays(nums1, nums2):
    #lol this is horrible code
    #if either are empty
    if len(nums1) == 0:
        return median(nums2)
    if len(nums2) == 0:
        return median(nums1)
    outnums = []
    totalLen = len(nums1) + len(nums2)
    if totalLen % 2 == 0:
        isEven = True
    else:
        isEven = False
    if isEven:
        outNumsSize = int(totalLen / 2)
        num1Pos = num2Pos = 0
        for i in range(outNumsSize):
            if i == outNumsSize-1:
                if num1Pos == len(nums1):
                    med1 = nums2[num2Pos]
                    num2Pos += 1
                    break
                if num2Pos == len(nums2):
                    med1 = nums1[num1Pos]
                    num1Pos += 1
                    break
                if nums1[num1Pos] < nums2[num2Pos]:
                    med1 = nums1[num1Pos]
                    num1Pos += 1
                    break
                else:
                    med1 = nums2[num2Pos]
                    num2Pos += 1
                    break
            if num1Pos == len(nums1):
                num2Pos += 1
                continue
            if num2Pos == len(nums2):
                num1Pos += 1
                continue
            if nums1[num1Pos] < nums2[num2Pos]:
                num1Pos += 1
            else:
                num2Pos += 1
        if num1Pos == len(nums1):
            med2 = nums2[num2Pos]
        elif num2Pos == len(nums2):
            med2 = nums1[num1Pos]
        else:
            if nums1[num1Pos] < nums2[num2Pos]:
                med2 = nums1[num1Pos]
            else:
                med2 = nums2[num2Pos]
        return (med1 + med2) / 2
    else:
        outNumsSize = math.ceil(totalLen/2)
        num1Pos = num2Pos = 0
        for i in range(outNumsSize):
            if i == outNumsSize-1:
                if num1Pos == len(nums1):
                    return nums2[num2Pos]
                if num2Pos == len(nums2):
                    return nums1[num1Pos]
                if nums1[num1Pos] < nums2[num2Pos]:
                    return nums1[num1Pos]
                else:
                    return nums2[num2Pos]
            if num1Pos == len(nums1):
                num2Pos += 1
                continue
            if num2Pos == len(nums2):
                num1Pos += 1
                continue
            if nums1[num1Pos] < nums2[num2Pos]:
                num1Pos += 1
            else:
                num2Pos += 1

input1 = input().split()
input2 = input().split()
nums1 = [int(x) for x in input1]
nums2 = [int(x) for x in input2]
print(findMedianSortedArrays(nums1, nums2))