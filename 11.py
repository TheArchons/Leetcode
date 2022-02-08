def topTwo(height):
    one, two = 0, len(height)-1
    maxArea = 0
    while one != two:
        area = (two-one)*min(height[one], height[two])
        if area > maxArea:
            maxArea = area
        if height[one] < height[two]:
            one += 1
        else:
            two -= 1
    return maxArea


ins = input().strip('[]')
height = [int(i) for i in ins.split(',')]
print(topTwo(height))
#1, 2, 3, 4, 6, 9, 12, 18, 36