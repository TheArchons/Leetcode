def inOrder(root):
    # Write your code here
    visited = set()
    prev = []
    res = []

    prev.append(-1)  # extra value to traverse to the other side of the parent node
    prev.append(root)
    res.append(root.info)
    curr = root
    while (len(prev) > 0):
        if curr.left is not None and curr.left not in visited:
            curr = curr.left
            res.append(curr.info)
            prev.append(curr)
            visited.add(curr)

        elif curr.right is not None and curr.right not in visited:
            curr = curr.right
            res.append(curr.info)
            prev.append(curr)
            visited.add(curr)

        else:
            curr = prev[-1]
            prev.pop()

    [print(x, end=" ") for x in sorted(res)]