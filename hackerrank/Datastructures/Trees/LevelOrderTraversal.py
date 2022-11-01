from collections import deque

def levelOrder(root):
    # Just BFS
    q = deque()
    q.append(root)

    while (len(q) != 0):
        curr = q.popleft()
        print(curr.info, end=" ")
        if (curr.left is not None):
            q.append(curr.left)
        if (curr.right is not None):
            q.append(curr.right)
    
    return