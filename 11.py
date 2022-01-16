def maxArea(height):
    topArea = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            if i == j:
               continue
            area = min(height[i], height[j]) * (j - i)
            if area > topArea:
                topArea = area
    return topArea

ins = input()
height = [int(i) for i in ins.split(',')]
print(maxArea(height))