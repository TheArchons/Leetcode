# wtf did I write here (was done a year ago)

def hourglassSum(arr):
    # Write your code here
    oneRow1, oneRow2, oneRow3, twoRow2, threeRow1, threeRow2, threeRow3 = 0, 1, 2, 1, 0, 1, 2
    currentHighestRow = 0
    currentHourglassSum = 0
    highestHourglassSum = float('-inf')
    while currentHighestRow < 4:
        while oneRow3 <= 5:
            currentHourglassSum += arr[currentHighestRow][oneRow1] + arr[currentHighestRow][oneRow2] + arr[currentHighestRow][oneRow3] + arr[currentHighestRow+1][twoRow2] + arr[currentHighestRow+2][threeRow1] + arr[currentHighestRow+2][threeRow2] + arr[currentHighestRow+2][threeRow3]
            if currentHourglassSum > highestHourglassSum:
                highestHourglassSum = currentHourglassSum
            oneRow1, oneRow2, oneRow3, twoRow2, threeRow1, threeRow2, threeRow3 = oneRow1+1, oneRow2+1, oneRow3+1, twoRow2+1, threeRow1+1, threeRow2+1, threeRow3+1
            currentHourglassSum = 0
        else:
            currentHighestRow += 1
            oneRow1, oneRow2, oneRow3, twoRow2, threeRow1, threeRow2, threeRow3 = 0, 1, 2, 1, 0, 1, 2
    return highestHourglassSum