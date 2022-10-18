def equalStacks(h1, h2, h3):
    heights = [sum(h1), sum(h2), sum(h3)]
    while heights[0] != heights[1] or heights[1] != heights[2]:
        max_height = max(heights)
        max_index = heights.index(max_height)
        if max_index == 0:
            heights[0] -= h1.pop(0)
        elif max_index == 1:
            heights[1] -= h2.pop(0)
        else:
            heights[2] -= h3.pop(0)
    
    return heights[0]