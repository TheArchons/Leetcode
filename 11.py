def maxArea(height):
    topArea = min(height[0],height[-1]) * (len(height)-1)
    hLen = len(height)
    for i in reversed(range(2, hLen)):
        for j in range(hLen-i+1):
            #make efficent
            curr = height[j:i+j]
            val1 = curr[0]
            val2 = curr[-1]
            area = min(val1,val2) * (i-1)
            if area > topArea:
                topArea = area
    return topArea

ins = input()
height = [int(i) for i in ins.split(',')]
print(maxArea(height))
#1, 2, 3, 4, 6, 9, 12, 18, 36