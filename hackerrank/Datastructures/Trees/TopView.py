def topView(root):
    prev = [[root, False]]
    visited = set()
    curr = root
    vertical = horizontal = 0
    heights = {}
    while (len(prev) != 0):
        if (horizontal not in heights or heights[horizontal][1] < vertical):
            heights[horizontal] = (curr.info, vertical)
        if (curr.left is not None and curr.left not in visited):
            curr = curr.left
            prev.append([curr, True])
            visited.add(curr)
            horizontal -= 1
            vertical -= 1
        elif (curr.right is not None and curr.right not in visited):
            curr = curr.right
            prev.append([curr, False])
            visited.add(curr)
            horizontal += 1
            vertical -= 1
        else:
            if (prev[-1][1]):
                horizontal += 1
            else:
                horizontal -= 1
            prev.pop()
            if (len(prev) != 0):
                curr = prev[-1][0]
                vertical += 1
        
    for i in sorted(heights):
        print(heights[i][0], end=" ")