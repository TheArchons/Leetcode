import math

def findMedianSortedArrays(nums1, num2):
    outnums = []
    totalLen = len(nums1) + len(num2)
    if totalLen % 2 == 0:
        isEven = True
    else:
        isEven = False
    if isEven:
        outNumsSize = int((totalLen / 2) - 1)
        num1Pos = num2Pos = 0
        for i in range(outNumsSize):
            if i == outNumsSize-1:
                if nums1[num1Pos] < num2[num2Pos]:
                    med1 = nums1[num1Pos]
                    num1Pos += 1
                else:
                    med1 = num2[num2Pos]
                    num2Pos += 1
            if nums1[num1Pos] < nums2[num2Pos]:
                num1Pos += 1
            else:
                num2Pos += 1
        if nums1[num1Pos] < num2[num2Pos]:
            med2 = nums1[num1Pos]
        else:
            med2 = num2[num2Pos]
        return (med1 + med2) / 2
    else:
        outNumsSize = math.ceil(totalLen/2)
        num1Pos = num2Pos = 0
        for i in range(outNumsSize):
            if i == outNumsSize-1:
                if nums1[num1Pos] < num2[num2Pos]:
                    return nums1[num1Pos]
                else:
                    return num2[num2Pos]
            if nums1[num1Pos] < num2[num2Pos]:
                num1Pos += 1
            else:
                num2Pos += 1

input1 = input().split()
input2 = input().split()
nums1 = [int(x) for x in input1]
nums2 = [int(x) for x in input2]
print(findMedianSortedArrays(nums1, nums2))