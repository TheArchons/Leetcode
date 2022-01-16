def topTwo(array):
    top1 = array[0]
    top2 = array[0]
    top1Pos = 0
    top2Pos = 0
    for i in range(1,len(array)):
        if array[i] > top1:
            top2 = top1
            top2Pos = top1Pos
            top1 = array[i]
            top1Pos = i
        elif array[i] > top2:
            top2 = array[i]
            top2Pos = i
    return top1Pos, top2Pos

def maxArea(height):
    topArea = min(height[0],height[-1]) * (len(height)-1)
    hLen = len(height)
    topHeights = topTwo(height)
    print(topHeights[0], topHeights[1])
    for i in reversed(range(1, hLen)):
        for j in range(hLen-i):
            print(j, i+j)
            if j > topHeights[0] and i+j < topHeights[1]:
                continue
            #make efficent
            area = min(height[j], height[i+j]) * (i)
            if area > topArea:
                topArea = area
    return topArea

ins = input()
height = [int(i) for i in ins.split(',')]
print(maxArea(height))
#1, 2, 3, 4, 6, 9, 12, 18, 36